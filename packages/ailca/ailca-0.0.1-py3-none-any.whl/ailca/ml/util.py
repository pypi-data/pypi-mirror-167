import os
import json
import torch
from typing import Union
from ailca.core.env import *
from ailca.data.base import Dataset
from ailca.data.multimodal import MultimodalDataset
from ailca.ml.base import Model
from ailca.ml.base import PyTorchModel


class MLResult:
    def __init__(self,
                 model: Model,
                 dataset_train: Dataset,
                 dataset_test: Dataset = None):
        self.model = model
        self.dataset_train = dataset_train
        self.dataset_test = dataset_test

    def save(self,
             dir_name: str):
        """
        Save machine learning results.

        :param dir_name: (*str*) The name of the directory to store machine learning results.
        """

        # Make a directory to store machine learning results.
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        # Store metadata of the prediction model.
        exp_info = dict()
        exp_info['alg_id'] = self.model.alg_id
        exp_info['alg_name'] = self.model.alg_name
        exp_info['alg_src'] = self.model.alg_src

        # Store metadata of the dataset.
        if isinstance(self.dataset_train, MultimodalDataset):
            for i in range(0, len(self.dataset_train.datasets)):
                exp_info['dataset' + str(i) + '_metadata'] = self.dataset_train.datasets[i].metadata
        else:
            exp_info['dataset_metadata'] = self.dataset_train.metadata

        # Store the machine learning results on the training dataset.
        preds_train = self.model.predict(self.dataset_train)
        exp_info['mae_train'] = mae(self.dataset_train.y, preds_train)
        exp_info['r2_train'] = r2_score(self.dataset_train.y, preds_train)

        # Store the machine learning results on the test dataset if it is available.
        if self.dataset_test is not None:
            exp_info['preds_test'] = self.model.predict(self.dataset_test)
            exp_info['mae_test'] = mae(self.dataset_test.y, exp_info['preds_test'])
            exp_info['r2_test'] = r2_score(self.dataset_test.y, exp_info['preds_test'])
            exp_info['targets_test'] = self.dataset_test.y.flatten().tolist()
            exp_info['preds_test'] = exp_info['preds_test'].flatten().tolist()

        # Save the JSON file to store the metadata.
        with open(dir_name + '/exp_info.json', 'w') as f:
            json.dump(exp_info, f)

        # Save the model parameters.
        self.model.save(dir_name + '/pred_model.pt')


def get_optimizer(model: PyTorchModel,
                  gradient_method: str,
                  init_lr: float = 1e-3,
                  l2_reg: float = 1e-6) -> torch.optim.Optimizer:
    """
    Get a gradient-based optimizer to fit the model parameters of neural networks.

    :param model: (*PyTorchModel*) A model to be optimized.
    :param gradient_method: (*str*) A name of the gradient method.
    :param init_lr: (*float, optional*) Initial learning rate of the gradient-based optimizer (*default* = 1e-6).
    :param l2_reg: (*float, optional*) L2 regularization coefficient to prevent the overfitting problem.
    :return: (*torch.optim.Optimizer*) A gradient-based optimizer.
    """

    if gradient_method == GD_SGD:
        return torch.optim.SGD(model.parameters(), lr=init_lr, weight_decay=l2_reg, momentum=0.9)
    elif gradient_method == GD_ADADELTA:
        return torch.optim.Adadelta(model.parameters(), lr=init_lr, weight_decay=l2_reg)
    elif gradient_method == GD_RMSPROP:
        return torch.optim.RMSprop(model.parameters(), lr=init_lr, weight_decay=l2_reg)
    elif gradient_method == GD_ADAM:
        return torch.optim.Adam(model.parameters(), lr=init_lr, weight_decay=l2_reg)
    else:
        raise AssertionError('Unknown gradient method {} was given.'.format(gradient_method))


def get_loss_func(loss_func: str) -> Union[torch.nn.L1Loss, torch.nn.MSELoss, torch.nn.SmoothL1Loss]:
    """
    Get a loss function object to run the gradient-based optimizers.

    :param loss_func: (*str*) A name of the loss function.
    :return: (*Union[torch.nn.L1Loss, torch.nn.MSELoss, torch.nn.SmoothL1Loss]*) A loss function object.
    """

    if loss_func == LOSS_MAE:
        return torch.nn.L1Loss()
    elif loss_func == LOSS_MSE:
        return torch.nn.MSELoss()
    elif loss_func == LOSS_SMAE:
        return torch.nn.SmoothL1Loss()
    else:
        raise AssertionError('Unknown loss function {} was given.'.format(loss_func))


def mae(targets: torch.Tensor,
        preds: torch.Tensor) -> float:
    """
    Calculate mean absolute error (MAE) of the given ``targets`` and ``preds``.

    :param targets: (*torch.Tensor*) Target values.
    :param preds: (*torch.Tensor*) Predicted values.
    :return: (*float*) Calculated mean absolute error.
    """

    return torch.mean(torch.abs(targets - preds)).item()


def rmse(targets: torch.Tensor,
         preds: torch.Tensor) -> float:
    """
    Calculate root-mean-square error (RMSE) of the given ``targets`` and ``preds``.

    :param targets: (*torch.Tensor*) Target values.
    :param preds: (*torch.Tensor*) Predicted values.
    :return: (*float*) Calculated root-mean-square error.
    """

    return torch.sqrt(torch.mean((targets - preds)**2)).item()


def r2_score(targets: torch.Tensor,
             preds: torch.Tensor) -> float:
    """
    Calculate r2-score (coefficient of determination) of the given ``targets`` and ``preds``.

    :param targets: (*torch.Tensor*) Target values.
    :param preds: (*torch.Tensor*) Predicted values.
    :return: (*float*) Calculated r2-score.
    """

    target_mean = torch.mean(targets)
    ss_tot = torch.sum((targets - target_mean)**2)
    ss_res = torch.sum((targets - preds)**2)

    return (1 - ss_res / ss_tot).item()
