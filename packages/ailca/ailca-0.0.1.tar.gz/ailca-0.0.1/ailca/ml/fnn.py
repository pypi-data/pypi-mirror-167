"""
Feedforward Neural Networks
---------------------------
The ``ailca.ml.fnn`` module provides an implementation of the most essential feedforward neural network.
The algorithms in this module are used to predict target values from the feature vectors and the chemical formulas.
"""


import torch.utils.data
import torch.nn as nn
from torch.utils.data import DataLoader
from ailca.core.sys import *
from ailca.data.base import Dataset
from ailca.ml.base import PyTorchModel
from ailca.ml.nn import *


class FCLayer(Layer):
    def __init__(self,
                 dim_in: int,
                 dim_out: int,
                 batch_norm: bool = False,
                 act_func: str = None):
        super(FCLayer, self).__init__()
        self._modules.append(nn.Linear(dim_in, dim_out))
        self._dim_out = dim_out

        # Construct a batch normalization layer.
        if batch_norm:
            self._modules.append(nn.BatchNorm1d(dim_out))

        # Apply an activation function.
        if act_func is not None:
            self._modules.append(get_act_func(act_func))


class FNN(PyTorchModel):
    """
    A base class of feedforward neural networks.
    """

    @abstractmethod
    def __init__(self,
                 alg_name: str,
                 layers: list):
        super(FNN, self).__init__(alg_name)
        self._layers = layers_to_sequential(layers)
        self._dim_out = layers[-1].dim_out

    @abstractmethod
    def forward(self,
                x: object) -> torch.Tensor:
        """
        Execute the forward process of the prediction model.

        :param x: (*object*) Input data of the model.
        :return: (*torch.Tensor*) Output of the model for the input data.
        """

        pass

    def fit(self,
            data_loader: DataLoader,
            optimizer: torch.optim.Optimizer,
            loss_func: torch.nn.Module) -> float:
        """
        Optimize the model parameters of the prediction model to minimize the given ``loss_func``.

        :param data_loader: (*DataLoader*) A data loader object for generating mini-batches from the training dataset.
        :param optimizer: (*torch.optim.Optimizer*) An optimization algorithm to fit the model parameters.
        :param loss_func: (*torch.nn.Module*) A loss function to fit the model parameters.
        :return: (*float*) Training loss.
        """

        # Initialize training loss.
        train_loss = 0

        # Set the model to the training mode.
        self.train()

        # Train the machine learning model for each mini-batch.
        for x, y in data_loader:
            # Move the data from CPU to GPU if GPU is runnable.
            if is_gpu_runnable():
                x = x.cuda()
                y = y.cuda()

            # Predict target values for the input data.
            y_p = self(x)

            # Calculate the training loss for the mini-batch.
            loss = loss_func(y_p, y)

            # Optimize the model parameters.
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Accumulate the training loss.
            train_loss += loss.item()

        return train_loss / len(data_loader)

    def predict(self,
                dataset: Dataset) -> torch.Tensor:
        """
        Predict the target values for the input data ``x``.

        :param dataset: (*Dataset*) A dataset containing the input data.
        :return: (*torch.Tensor*) Predicted values for the input dataset.
        """

        # Set the model to the evaluation model.
        self.eval()

        # Predict the target values for the given dataset.
        with torch.no_grad():
            if is_gpu_runnable():
                return self(dataset.x.cuda()).cpu()
            else:
                return self(dataset.x).cpu()


class FCNN(FNN):
    """
    A neural network to predict target values from vector- or matrix-shaped input data.
    It is trained to minimize the prediction errors that is usually defined as a distance metric
    between the true and predicted target values.
    """

    def __init__(self,
                 layers: list = None,
                 dim_in: int = None,
                 dim_out: int = None):
        if layers is None:
            if dim_in is None or dim_out is None:
                raise AssertionError('For auto-configuration of the network, dimensionalities of the input and target'
                                     'data must be provided by \'dim_in\' and \'dim_target\'.')

            super(FCNN, self).__init__(ALG_FCNN, [
                FCLayer(dim_in, 256, batch_norm=True, act_func=ACT_FUNC_RELU),
                FCLayer(256, 256, batch_norm=True, act_func=ACT_FUNC_RELU),
                FCLayer(256, dim_out)
            ])
        else:
            super(FCNN, self).__init__(ALG_FCNN, layers)

    def forward(self,
                inputs: torch.Tensor):
        """
        A forward process of neural networks.
        For input data in ``data``, it returns predicted target values.

        :param inputs: (*torch.Tensor*) Input data of the model.
        :return: (*numpy.ndarray*) Predicted target values.
        """

        return self._layers(inputs)
