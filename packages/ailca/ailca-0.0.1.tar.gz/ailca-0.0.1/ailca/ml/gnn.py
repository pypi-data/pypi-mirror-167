import torch.nn
import torch_geometric.data
from typing import Union
from torch.utils.data import DataLoader
from torch_geometric.data import Batch
from torch_geometric.nn import Sequential
from torch_geometric.nn import LayerNorm
from torch_geometric.nn import GCNConv
from torch_geometric.nn import GATConv
from torch_geometric.nn import GINConv
from torch_geometric.nn import NNConv
from torch_geometric.nn import CGConv
from torch_geometric.nn import TransformerConv
from torch_geometric.nn import global_mean_pool
from torch_geometric.nn import global_add_pool
from ailca.core.sys import is_gpu_runnable
from ailca.data.base import Dataset
from ailca.ml.base import PyTorchModel
from ailca.ml.nn import *
from ailca.ml.fnn import FCLayer


class GNNLayer(Layer):
    """
    A base class for the network layers of graph neural networks.
    """

    def __init__(self,
                 node_aggr_scheme: str,
                 dim_in_node: int,
                 dim_out: int,
                 dim_in_edge: int = None,
                 layer_norm: bool = False,
                 act_func: str = None):
        super(GNNLayer, self).__init__()
        self.__node_aggr_scheme = node_aggr_scheme
        self.__edge_aggr = False if dim_in_edge is None else True
        self._dim_out = dim_out

        if self.__node_aggr_scheme == ALG_GCN:
            self._modules.append((GCNConv(dim_in_node, dim_out), 'x, edge_index -> x'))
        elif self.__node_aggr_scheme == ALG_GAT:
            self._modules.append((GATConv(dim_in_node, dim_out), 'x, edge_index -> x'))
        elif self.__node_aggr_scheme == ALG_GIN:
            fcn = torch.nn.Linear(dim_in_node, dim_out)
            self._modules.append((GINConv(fcn), 'x, edge_index -> x'))
        elif self.__node_aggr_scheme == ALG_ECCNN:
            fce = torch.nn.Sequential(torch.nn.Linear(dim_in_edge, 64),
                                      torch.nn.ReLU(),
                                      torch.nn.Linear(64, dim_in_node * dim_out))
            self._modules.append((NNConv(dim_in_node, dim_out, fce), 'x, edge_index, edge_attr -> x'))
        elif self.__node_aggr_scheme == ALG_CGCNN:
            self._modules.append((CGConv(dim_in_node, dim_in_edge), 'x, edge_index, edge_attr -> x'))
        elif self.__node_aggr_scheme == ALG_TFGNN:
            self._modules.append((TransformerConv(dim_in_node, dim_out, edge_dim=dim_in_edge),
                                  'x, edge_index, edge_attr -> x'))
        else:
            raise AssertionError('Unknown node aggregation scheme \'{}\' was given.'.format(self.__node_aggr_scheme))

        if layer_norm:
            self._modules.append(LayerNorm(dim_out))

        if act_func is not None:
            self._modules.append(get_act_func(act_func))

    @property
    def edge_aggr(self):
        return self.__edge_aggr


class GNN(PyTorchModel):
    def __init__(self,
                 alg_name: str,
                 aggr_layers: list,
                 pred_layers: list,
                 readout_method: str = None,
                 node_emb_layers: list = None):
        super(GNN, self).__init__(alg_name)
        self.__edge_aggr = aggr_layers[0].edge_aggr
        self._aggr_layers = aggr_layers_to_sequential(aggr_layers, self.__edge_aggr)
        self._pred_layers = layers_to_sequential(pred_layers)
        self._node_emb_layers = None if node_emb_layers is None else layers_to_sequential(node_emb_layers)
        self._readout_method = readout_method
        self._dim_out = pred_layers[-1].dim_out

    def _readout(self,
                 node_embs: torch.Tensor,
                 batch_idx: torch.Tensor) -> torch.Tensor:
        if self._readout_method == READOUT_MEAN:
            return global_mean_pool(node_embs, batch_idx)
        elif self._readout_method == READOUT_SUM:
            return global_add_pool(node_embs, batch_idx)
        else:
            raise AssertionError('Unknown readout method {}.'.format(self._readout_METHOD))

    def forward(self,
                x: Union[Batch, torch_geometric.data.Data]) -> torch.Tensor:
        # Feature embedding layer(s).
        if self._node_emb_layers is not None:
            node_feats = self._node_emb_layers(x.x)
        else:
            node_feats = x.x

        # Node aggregation layer(s).
        if self.__edge_aggr:
            h = self._aggr_layers(node_feats, x.edge_index, x.edge_attr)
        else:
            h = self._aggr_layers(node_feats, x.edge_index)

        # Readout.
        if self._readout_method is not None:
            h = self._readout(h, x.batch)

        # Prediction layer(s).
        out = self._pred_layers(h)

        return out

    def fit(self,
            data_loader: DataLoader,
            optimizer: torch.optim.Optimizer,
            loss_func: torch.nn.Module) -> float:
        self.train()
        train_loss = 0

        for batch, y in data_loader:
            if is_gpu_runnable():
                batch = batch.cuda()
                y = y.cuda()

            y_p = self(batch)
            loss = loss_func(y_p, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_loss += loss.detach().item()

        return train_loss / len(data_loader)

    def predict(self,
                x: Dataset) -> torch.Tensor:
        self.eval()
        batch = Batch.from_data_list(x.x)

        with torch.no_grad():
            if is_gpu_runnable():
                batch = batch.cuda()

                return self(batch).cpu()
            else:
                return self(batch)


class GCN(GNN):
    def __init__(self,
                 dim_in_node: int,
                 dim_out: int,
                 readout_method: str = None):
        aggr_layers = [
            GNNLayer(node_aggr_scheme=ALG_GCN, dim_in_node=dim_in_node, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_GCN, dim_in_node=256, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_GCN, dim_in_node=256, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU)
        ]
        pred_layers = [
            FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=128, dim_out=dim_out)
        ]
        super(GCN, self).__init__(ALG_GCN, aggr_layers, pred_layers, readout_method)


class GAT(GNN):
    def __init__(self,
                 dim_in_node: int,
                 dim_out: int,
                 readout_method: str = None):
        aggr_layers = [
            GNNLayer(node_aggr_scheme=ALG_GAT, dim_in_node=dim_in_node, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_GAT, dim_in_node=256, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_GAT, dim_in_node=256, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU)
        ]
        pred_layers = [
            FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=128, dim_out=dim_out)
        ]
        super(GAT, self).__init__(ALG_GAT, aggr_layers, pred_layers, readout_method)


class GIN(GNN):
    def __init__(self,
                 dim_in_node: int,
                 dim_out: int,
                 readout_method: str = None):
        aggr_layers = [
            GNNLayer(node_aggr_scheme=ALG_GIN, dim_in_node=dim_in_node, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_GIN, dim_in_node=256, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_GIN, dim_in_node=256, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU)
        ]
        pred_layers = [
            FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=128, dim_out=dim_out)
        ]
        super(GIN, self).__init__(ALG_GIN, aggr_layers, pred_layers, readout_method)


class ECCNN(GNN):
    def __init__(self,
                 dim_in_node: int,
                 dim_in_edge: int,
                 dim_out: int,
                 readout_method: str = None):
        aggr_layers = [
            GNNLayer(node_aggr_scheme=ALG_ECCNN, dim_in_node=dim_in_node, dim_in_edge=dim_in_edge, dim_out=128,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_ECCNN, dim_in_node=128, dim_in_edge=dim_in_edge, dim_out=64,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_ECCNN, dim_in_node=64, dim_in_edge=dim_in_edge, dim_out=64,
                     layer_norm=True, act_func=ACT_FUNC_PRELU)
        ]
        pred_layers = [
            FCLayer(dim_in=64, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=128, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=128, dim_out=dim_out)
        ]
        super(ECCNN, self).__init__(ALG_ECCNN, aggr_layers, pred_layers, readout_method)


class CGCNN(GNN):
    def __init__(self,
                 dim_in_node: int,
                 dim_in_edge: int,
                 dim_out: int,
                 readout_method: str = None):
        node_emb_layers = [
            FCLayer(dim_in=dim_in_node, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU)
        ]
        aggr_layers = [
            GNNLayer(node_aggr_scheme=ALG_CGCNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_CGCNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_CGCNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU)
        ]
        pred_layers = [
            FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=128, dim_out=dim_out)
        ]
        super(CGCNN, self).__init__(ALG_CGCNN, aggr_layers, pred_layers, readout_method, node_emb_layers)


class TFGNN(GNN):
    def __init__(self,
                 dim_in_node: int,
                 dim_in_edge: int,
                 dim_out: int,
                 readout_method: str = None):
        aggr_layers = [
            GNNLayer(node_aggr_scheme=ALG_TFGNN, dim_in_node=dim_in_node, dim_in_edge=dim_in_edge, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_TFGNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU),
            GNNLayer(node_aggr_scheme=ALG_TFGNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                     layer_norm=True, act_func=ACT_FUNC_PRELU)
        ]
        pred_layers = [
            FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
            FCLayer(dim_in=128, dim_out=dim_out)
        ]
        super(TFGNN, self).__init__(ALG_TFGNN, aggr_layers, pred_layers, readout_method)


def aggr_layers_to_sequential(list_layers: list,
                              contain_edge_feats: bool) -> Sequential:
    metadata = 'x, edge_index, edge_attr' if contain_edge_feats else 'x, edge_index'
    listed_layers = list()

    for layer in list_layers:
        for module in layer.tolist():
            listed_layers.append(module)

    return Sequential(metadata, listed_layers)
