from __future__ import annotations
import numpy
import torch
import torch.utils.data
from typing import Union
from typing import Tuple
from math import isnan
from copy import deepcopy
from ailca.core.operation import sublist
from ailca.core.operation import split_list
from ailca.core.operation import merge_lists
from ailca.data.base import Dataset


class MultimodalDataset(torch.utils.data.Dataset):
    """
    A dataset class to store heterogeneous datasets for multimodal learning.
    """

    def __init__(self,
                 datasets: list,
                 targets: torch.Tensor = None):
        self.datasets = datasets
        self.y = None if targets is None else targets
        self.data = list()

        for i in range(0, len(self.datasets[0])):
            self.data.append([dataset.data[i] for dataset in self.datasets])

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self,
                    idx: int) -> Union[Tuple[list, None], Tuple[list, torch.Tensor]]:
        if self.y is None:
            return [d.x for d in self.data[idx]], None
        else:
            return [d.x for d in self.data[idx]], self.y[idx]

    def clone(self,
              new_data: list = None,
              new_targets: torch.Tensor = None) -> MultimodalDataset:
        """
        Generate a clone of the dataset.
        If new data is given through ``new_data``, a new dataset with copied metadata is generated.

        :param new_data: (*list, optional*) New data to be stored the copied dataset (*default* = ``None``).
        :param new_targets: (*torch.Tensor*) New target data (*default* = ``None``).
        :return: (*MultimodalDataset*) A copied dataset.
        """

        if new_data is None:
            return deepcopy(self)
        else:
            new_datasets = list()
            for i in range(0, len(self.datasets)):
                new_datasets.append(Dataset([d[i] for d in new_data]))

            return MultimodalDataset(new_datasets, new_targets)

    def split(self,
              ratio: float,
              random_seed: int = None) -> Tuple[MultimodalDataset, MultimodalDataset]:
        """
        Split the dataset into two sub-datasets.
        In this function, the data objects are divided into two sub-data, but the metadata of the dataset is preserved.

        :param ratio: (*float*) A ratio of the number data in the two sub-datasets. Note that it must be in (0, 1).
        :param random_seed: (*int, optional*) A random seed to split the dataset (*default* = ``None``).
        :return: (*Tuple[MultimodalDataset, MultimodalDataset]*) Two sub-datasets of the original dataset.
        """

        if ratio >= 1 or ratio <= 0:
            raise ValueError('The radio must be in [0, 1], but the given ratio is {:.4f}'.format(ratio))

        if random_seed is not None:
            numpy.random.seed(random_seed)

        n_dataset1 = int(ratio * len(self))
        idx_rand = numpy.random.permutation(len(self))
        new_data1 = sublist(self.data, idx_rand[:n_dataset1])
        new_data2 = sublist(self.data, idx_rand[n_dataset1:])
        new_targets1 = None
        new_targets2 = None

        if self.y is not None:
            new_targets1 = self.y[idx_rand[:n_dataset1]]
            new_targets2 = self.y[idx_rand[n_dataset1:]]

        dataset1 = self.clone(new_data=new_data1, new_targets=new_targets1)
        dataset2 = self.clone(new_data=new_data2, new_targets=new_targets2)

        return dataset1, dataset2

    def save(self,
             path: str):
        """
        Save the dataset in a given ``path``.

        :param path: (*str*) Path of the saved dataset.
        """

        torch.save(self, path)

    @staticmethod
    def load(path: str) -> MultimodalDataset:
        """
        Load the dataset from a given ``path``.

        :param path: (*str*) Path of the dataset.
        :return: (*MultimodalDataset*) A dataset object.
        """

        return torch.load(path)

    def complete(self) -> MultimodalDataset:
        """
        Remove the data of the missing values in the target data.

        :return: (*MultimodalDataset*) A refined dataset without missing values in the target data.
        """

        new_data = list()
        new_targets = list()

        for i in range(0, self.y.shape[0]):
            if not isnan(self.y[i]):
                new_data.append(self.data[i])
                new_targets.append(self.y[i])

        return self.clone(new_data=new_data, new_targets=torch.vstack(new_targets))

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
        sub_targets = [self.y[idx] for idx in idx_rand]
        k_folds = list()

        # Generate k tuples of the training and test datasets from the k subsets.
        for i in range(0, k):
            data_train = merge_lists(sub_data[:i], sub_data[i+1:])
            targets_train = torch.vstack(merge_lists(sub_targets[:i], sub_targets[i+1:]))
            data_test = sub_data[i]
            targets_test = sub_targets[i]
            dataset_train = self.clone(new_data=data_train, new_targets=targets_train)
            dataset_test = self.clone(new_data=data_test, new_targets=targets_test)
            k_folds.append([dataset_train, dataset_test])

        return k_folds
