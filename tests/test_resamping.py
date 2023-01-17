import numpy as np
from cellmapping.resampling import downsample_3d_array


def test_downsample_3d_array():
    # Test Case 1: Downsample a small 3D array
    # create a random 3D array with shape (4, 4, 3)
    array = np.random.rand(4, 4, 3)
    target_size = (2, 2, 3)
    downsampled_array = downsample_3d_array(array, target_size)
    assert downsampled_array.shape == target_size, f"Expected shape {target_size}, but got {downsampled_array.shape}"

    # Test Case 2: Downsample a large 3D array
    # create a random 3D array with shape (256, 256, 3)
    array = np.random.rand(256, 256, 3)
    target_size = (128, 128, 3)
    downsampled_array = downsample_3d_array(array, target_size)
    assert downsampled_array.shape == target_size, f"Expected shape {target_size}, but got {downsampled_array.shape}"

    # Test Case 3: Downsample a 3D array with non-square shape
    # create a random 3D array with shape (256, 512, 3)
    array = np.random.rand(256, 512, 3)
    target_size = (128, 256, 3)
    downsampled_array = downsample_3d_array(array, target_size)
    assert downsampled_array.shape == target_size, f"Expected shape {target_size}, but got {downsampled_array.shape}"

    # Test Case 4: Downsample a 3D array with non-square shape and non-unit depth
    # create a random 3D array with shape (256, 512, 5)
    array = np.random.rand(256, 512, 5)
    target_size = (128, 256, 3)
    downsampled_array = downsample_3d_array(array, target_size)
    assert downsampled_array.shape == target_size, f"Expected shape {target_size}, but got {downsampled_array.shape}"
