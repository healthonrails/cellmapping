import numpy as np
from skimage.transform import resize


def downsample_3d_array(array, target_size):
    """Downsample a 3D numpy array to a target size.

    Parameters:
    - array (numpy.ndarray): The input 3D array.
    - target_size (tuple): The target size (height, width, depth).

    Returns:
    - downsampled_array (numpy.ndarray): The downsampled array.
    """
    downsampled_array = resize(array, target_size, order=3)
    return downsampled_array
