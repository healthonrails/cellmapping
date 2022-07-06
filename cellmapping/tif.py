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
