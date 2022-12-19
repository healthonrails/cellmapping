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
