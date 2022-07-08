import cv2
import numpy as np
from skimage.feature import blob_dog
from skimage.morphology import reconstruction


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
    cv2.imwrite('h_max_transform.png', img_h_max)
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


def find_maxima(img):
    """
    Find maxima in the image.
    """


def detect_cells(img):
    """
    Detect cells in the image.
    """
    # remove background
    img = remove_background(img)
    # filter with the DoG filter
    blobs = filter_dog(img)

    # find maxima

    # cell size

    return blobs
