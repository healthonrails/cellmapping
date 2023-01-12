import tifffile
import cv2
import numpy as np
from skimage.feature import blob_dog
from skimage.morphology import reconstruction
from scipy.ndimage.filters import maximum_filter


def h_max_transform(img, h_max):
    """
    Compute the H-max transformation of a image.
    img: image array
    h_max (float): h maximum value of the H-max transformation

    returns:
    img_h_max: H-max transformation of the image
    """
    if h_max is None:
        return img
    img_h_max = reconstruction(img - h_max, img, method='dilation')
    return img_h_max


def remove_background(img):
    """
    Subtracts the background from the 2d image
    """
    dtype = img.dtype
    img = np.array(img, dtype=float)

    disk = np.ones((3, 3), dtype=np.uint8)
    img -= cv2.morphologyEx(img, cv2.MORPH_OPEN, disk)
    img[img < 0]
    img = np.array(img, dtype=dtype)
    return img


def filter_dog(img,
               max_sigma=5,
               min_sigma=1,
               threshold=.1):
    """
    Filter the image with the DoG filter.
    """
    blobs = blob_dog(img, min_sigma=min_sigma,
                     max_sigma=max_sigma, threshold=threshold)
    return blobs


def find_maxima(
        img,
        size=5,
        h_max=None):
    """
    Find maxima in the image.
    """
    img_shape = img.shape
    if not isinstance(size, tuple):
        if len(img_shape) == 2:
            size = (size, size)
        elif len(img_shape) == 3:
            size = (size, size, size)
    if h_max and h_max > 0:
        img = h_max_transform(img, h_max)
    img_max = maximum_filter(img, size=size)
    return img_max == img


def detect_cells(signal_img_path,
                 background_img_path,
                 voxel_sizes=[5, 2, 2]):
    """
    Detect cells in the image.
    """
    from cellfinder_core.main import main as cellfinder_run

    signal_array = tifffile.imread(signal_img_path)
    background_array = tifffile.imread(background_img_path)

    # voxel_sizes = [5, 2, 2]  # in microns
    detected_cells = cellfinder_run(
        signal_array, background_array, voxel_sizes)
    return detected_cells
