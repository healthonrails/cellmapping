import cv2
import numpy as np
from skimage.feature import blob_dog


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
