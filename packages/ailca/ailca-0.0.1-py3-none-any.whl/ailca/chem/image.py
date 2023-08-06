"""
Image
-----
It provides functions to process and load the image data for machine learning.
"""


import torch
import numpy
import pandas
from tqdm import tqdm
from PIL import Image
from ailca.core.env import *
from ailca.data.base import Data
from ailca.data.base import Dataset


def load_dataset(path_metadata_file: str,
                 path_imgs: str,
                 idx_img_id: int,
                 idx_target: int = None,
                 ext_img: str = 'png',
                 verbose: bool = True) -> Dataset:
    """
    Load the dataset containing the numerical features.
    If ``idx_target`` is given, the dataset is loaded with the target values.

    :param path_metadata_file: (*str*) The path of the metadata file of the image data.
    :param path_imgs: (*str*) A directory of the image files.
    :param idx_img_id: (*int*) An index of the image identifiers in the metadata file.
    :param idx_target: (*int, optional*) An index of the target values in the data file (*default* = ``None``).
    :param ext_img: (*str, optional*) Extension of the image file (*default = ``png``).
    :param verbose: (*bool*) A flag variable to present the system log in data loading (*default* = ``True``).
    :return: (*Dataset*) A dataset object.
    """

    ext_img = '.' + ext_img
    metadata = numpy.array(pandas.read_excel(path_metadata_file))
    iter_range = range(0, metadata.shape[0])
    list_data = list()

    if verbose:
        iter_range = tqdm(iter_range)

    for i in iter_range:
        path_img_file = path_imgs + '/' + metadata[i, idx_img_id] + ext_img
        img = torch.tensor(numpy.array(Image.open(path_img_file).convert('RGB')), dtype=torch.float)

        # Swap axes the loaded image to fit the data format into the torchvision library.
        img = torch.swapaxes(img, 0, 2)

        if idx_target is None:
            list_data.append(Data(x=img, dtype=DTYPE_IMG))
        else:
            list_data.append(Data(x=img, y=metadata[i, idx_target], dtype=DTYPE_IMG))

    return Dataset(list_data, idx_img_id=idx_img_id, idx_target=idx_target, ext_img=ext_img)
