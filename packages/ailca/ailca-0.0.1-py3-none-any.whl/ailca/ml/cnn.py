import torch
import torch.nn.functional as F
import torchvision.models.resnet as resnet
import torchvision.models.densenet as densenet
import torchvision.models.regnet as regnet
from abc import ABCMeta
from abc import abstractmethod
from torch.utils.data import DataLoader
from ailca.core.env import *
from ailca.core.sys import is_gpu_runnable
from ailca.ml.base import PyTorchModel
from ailca.data.base import Dataset


class CNN(PyTorchModel):
    @abstractmethod
    def __init__(self,
                 alg_name: str,
                 dim_out: int):
        super(CNN, self).__init__(alg_name)
        self._dim_out = dim_out

    def fit(self,
            data_loader: DataLoader,
            optimizer: torch.optim.Optimizer,
            loss_func: torch.nn.Module):
        """
        Optimize the model parameters of the prediction model to minimize the given ``loss_func``.

        :param data_loader: (*DataLoader*) A data loader object for generating mini-batches from the training dataset.
        :param optimizer: (*torch.optim.Optimizer*) An optimization algorithm to fit the model parameters.
        :param loss_func: (*torch.nn.Module*) A loss function to fit the model parameters.
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


class ResNet(CNN, resnet.ResNet, metaclass=ABCMeta):
    def forward(self,
                x: torch.Tensor) -> torch.Tensor:
        """
        Execute the forward process of the prediction model.

        :param x: (*torch.Tensor*) Input data of the model.
        :return: (*torch.Tensor*) Output of the model for the input data.
        """

        return self._forward_impl(x)


class ResNet18(ResNet):
    def __init__(self, dim_out, **kwargs):
        CNN.__init__(self, ALG_RESNET18, dim_out)
        resnet.ResNet.__init__(self, resnet.BasicBlock, [2, 2, 2, 2], num_classes=dim_out, **kwargs)


class ResNet34(ResNet):
    def __init__(self, dim_out, **kwargs):
        CNN.__init__(self, ALG_RESNET18, dim_out)
        resnet.ResNet.__init__(self, resnet.BasicBlock, [3, 4, 6, 3], num_classes=dim_out, **kwargs)


class ResNet101(ResNet):
    def __init__(self, dim_out, **kwargs):
        CNN.__init__(self, ALG_RESNET18, dim_out)
        resnet.ResNet.__init__(self, resnet.BasicBlock, [3, 4, 23, 3], num_classes=dim_out, **kwargs)


class DenseNet(CNN, densenet.DenseNet, metaclass=ABCMeta):
    def forward(self,
                x: torch.Tensor) -> torch.Tensor:
        """
        Execute the forward process of the prediction model.

        :param x: (*torch.Tensor*) Input data of the model.
        :return: (*torch.Tensor*) Output of the model for the input data.
        """

        features = self.features(x)
        out = F.relu(features, inplace=True)
        out = F.adaptive_avg_pool2d(out, (1, 1))
        out = torch.flatten(out, 1)
        out = self.classifier(out)

        return out


class DenseNet121(DenseNet):
    def __init__(self, dim_out, **kwargs):
        CNN.__init__(self, ALG_DENSENET121, dim_out)
        densenet.DenseNet.__init__(self, 32, (6, 12, 24, 16), 64, num_classes=dim_out, **kwargs)


class RegNetY(CNN, regnet.RegNet, metaclass=ABCMeta):
    def forward(self,
                x: torch.Tensor) -> torch.Tensor:
        """
        Execute the forward process of the prediction model.

        :param x: (*torch.Tensor*) Input data of the model.
        :return: (*torch.Tensor*) Output of the model for the input data.
        """

        x = self.stem(x)
        x = self.trunk_output(x)

        x = self.avgpool(x)
        x = x.flatten(start_dim=1)
        x = self.fc(x)

        return x
