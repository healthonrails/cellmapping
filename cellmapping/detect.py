import numpy as np
from skimage.feature import blob_dog


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
