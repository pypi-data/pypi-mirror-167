"""
Base Module
-----------
This module defines base classes and functions to process the datasets in the file systems.
The implemented ``Dataset`` object provides useful methods to read the data from the dataset files.
"""


from __future__ import annotations
import numpy
import torch
import torch.utils.data
import torch_geometric.data
from typing import Union
from typing import Tuple
from math import isnan
from copy import deepcopy
from sklearn.preprocessing import scale
from ailca.core.env import *
from ailca.core.operation import sublist
from ailca.core.operation import split_list
from ailca.core.operation import merge_lists


class Data:
    """
    A base class to store the data.
    """

    def __init__(self,
                 x: Union[torch.Tensor, torch_geometric.data.Data],
                 y: float = None,
                 dtype: str = DTYPE_FVEC):
        self.x = deepcopy(x)
        self.y = None if y is None else torch.tensor(y, dtype=torch.float)
        self.__dtype = dtype

    @property
    def dtype(self):
        return self.__dtype


class Dataset(torch.utils.data.Dataset):
    """
    A base class to store the dataset.
    """

    def __init__(self,
                 data: list,
                 **kwargs):
        self.data = data
        self._x = None
        self._y = None if self.data[0].y is None else torch.vstack([d.y for d in self.data])
        self.metadata = deepcopy(kwargs)
        self.__dtype = self.data[0].dtype

        # For vector dataset.
        self.__dim_in = None

        # For graph dataset.
        self.__dim_in_node = None
        self.__dim_in_edge = None

        if isinstance(self.data[0].x, torch.Tensor):
            # For tensor dataset including feature vectors and images.
            self._x = torch.stack([d.x for d in self.data], dim=0)
            self.__dim_in = self._x.shape[1]
        elif isinstance(self.data[0].x, torch_geometric.data.Data):
            # For graph dataset.
            self._x = [d.x for d in self.data]
            self.__dim_in_node = data[0].x.x.shape[1]
            self.__dim_in_edge = data[0].x.edge_attr.shape[1]
        else:
            raise TypeError('Unsupported data type {} is in the \'Data\' object.'.format(self.data[0].x.__class__))

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx) -> Union[Tuple[torch.Tensor, None], Tuple[torch.Tensor, torch.Tensor]]:
        if self._y is None:
            return self._x[idx], None
        else:
            return self._x[idx], self._y[idx]

    @property
    def x(self) -> Union[torch.Tensor, list]:
        return self._x

    @property
    def y(self) -> Union[torch.Tensor, None]:
        return self._y

    @property
    def dim_in(self):
        return self.__dim_in

    @property
    def dim_in_node(self):
        return self.__dim_in_node

    @property
    def dim_in_edge(self):
        return self.__dim_in_edge

    @property
    def dtype(self):
        return self.__dtype

    def clone(self,
              new_data: list = None) -> Dataset:
        """
        Generate a clone of the dataset.
        If new data is given through ``new_data``, a new dataset with copied metadata is generated.

        :param new_data: (*list, optional*) New data to be stored the copied dataset (*default* = ``None``).
        :return: (*Dataset*) A copied dataset.
        """

        if new_data is None:
            return deepcopy(self)
        else:
            dataset = Dataset(new_data)
            dataset.metadata = self.metadata

            return dataset

    def split(self,
              ratio: float,
              random_seed: int = None) -> Tuple[Dataset, Dataset]:
        """
        Split the dataset into two sub-datasets.
        In this function, the data objects are divided into two sub-data, but the metadata of the dataset is preserved.

        :param ratio: (*float*) A ratio of the number data in the two sub-datasets. Note that it must be in (0, 1).
        :param random_seed: (*int, optional*) A random seed to split the dataset (*default* = ``None``).
        :return: (*Tuple[Dataset, Dataset]*) Two sub-datasets of the original dataset.
        """

        if ratio >= 1 or ratio <= 0:
            raise ValueError('The radio must be in [0, 1], but the given ratio is {:.4f}'.format(ratio))

        if random_seed is not None:
            numpy.random.seed(random_seed)

        n_dataset1 = int(ratio * len(self))
        idx_rand = numpy.random.permutation(len(self))
        dataset1 = self.clone(new_data=sublist(self.data, idx_rand[:n_dataset1]))
        dataset2 = self.clone(new_data=sublist(self.data, idx_rand[n_dataset1:]))

        return dataset1, dataset2

    def save(self,
             path: str):
        """
        Save the dataset in a given ``path``.

        :param path: (*str*) Path of the saved dataset.
        """

        torch.save(self, path)

    @staticmethod
    def load(path: str) -> Dataset:
        """
        Load the dataset from a given ``path``.

        :param path: (*str*) Path of the dataset.
        :return: (*Dataset*) A dataset object.
        """

        return torch.load(path)

    def normalize(self):
        """
        Normalize the input data of the dataset if the input data is a ``torch.Tensor`` object.
        """

        if not isinstance(self._x, torch.Tensor):
            raise TypeError('Only datasets containing \'torch.Tensor\' input data can be normalized.')

        self._x = scale(self._x)

    def complete(self) -> Dataset:
        """
        Remove the data of the missing values in the target data.

        :return: (*Dataset*) A refined dataset without missing values in the target data.
        """

        new_data = list()

        for i in range(0, self.y.shape[0]):
            if not isnan(self.y[i]):
                new_data.append(self.data[i])

        return self.clone(new_data=new_data)

    def get_k_folds(self,
                    k: int,
                    random_seed: int = None) -> list:
        """
        Generate ``k`` subsets of the dataset for k-fold cross-validation.

        :param k: (*int*) The number of subsets for k-fold cross-validation.
        :param random_seed: (*int, optional*) An integer index of the random seed (*default* = ``None``).
        :return: (*list*) A list of the k-folds.
        """

        if random_seed is not None:
            numpy.random.seed(random_seed)

        # Split the dataset into k subsets.
        idx_rand = numpy.array_split(numpy.random.permutation(len(self.data)), k)
        sub_data = split_list(self.data, k, idx_rand=idx_rand)
        k_folds = list()

        # Generate k tuples of the training and test datasets from the k subsets.
        for i in range(0, k):
            data_train = merge_lists(sub_data[:i], sub_data[i + 1:])
            data_test = sub_data[i]
            k_folds.append([Dataset(data_train), Dataset(data_test)])

        return k_folds
