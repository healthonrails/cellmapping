import glob
import os


def read_tiffs(
        folder_path,
        file_pattern='*.tif'):
    """Read and sort tiff files from the given folder.

    Parameters
    ----------
    folder_path : str
        folder path to the location of tiff files
    """
    tiffs = glob.glob(os.path.join(folder_path,
                                   file_pattern))
    tiffs = sorted(tiffs)
    return tiffs


def write_tiffs(ndarray,
                filename='atlas_100mn_brain_sagital.tif',
                photometric='minisblack'
                ):
    """Save numpy array as a tif file

    Args:
        ndarray (numpy.array): n dim numpy array
        filename (str, optional): File name. Defaults to 'atlas_100mn_brain_sagital.tif'.
        photometric (str, optional): photmetric. Defaults to 'minisblack'.
    """
    from tifffile import imwrite
    imwrite(filename, ndarray, photometric=photometric)


def resample_2d(img, target_shape=(320, 528)):
    """resample 2d image to the target size

    Args:
        img (2d numpy array): 2d image e.g. sagittal brain slice
        target_shape (tuple, optional): the target size e.g. to atlas size 
        (width, height)
         Defaults to (320, 528).

    Returns:
        numpy array: resized image
    """
    import cv2
    res = cv2.resize(img,
                     dsize=target_shape,
                     interpolation=cv2.INTER_CUBIC)
    return res
