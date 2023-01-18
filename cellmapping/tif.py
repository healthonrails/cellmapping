import glob
import os
import SimpleITK as sitk


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
                photometric='minisblack',
                save_16bit=True
                ):
    """Save numpy array as a tif file

    Args:
        ndarray (numpy.array): n dim numpy array
        filename (str, optional): File name. Defaults to 'atlas_100mn_brain_sagital.tif'.
        photometric (str, optional): photmetric. Defaults to 'minisblack'.
    """
    from tifffile import imwrite
    if save_16bit:
        ndarray = (ndarray / np.max(ndarray) * (2**16-1)).astype(np.uint16)
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


def downsample_image(image_path, atlas_path):
    """This function that takes the paths to 
    the input image and atlas image as inputs 
    and returns the downsampled image

    Args:
        image_path (str): path to the brain image
        atlas_path (str): path to the atlas image

    Returns:
        image : downsampled image
    """
    # Load the TIFF image
    image = sitk.ReadImage(image_path)

    # Load the atlas image
    atlas = sitk.ReadImage(atlas_path)

    # Get the size of the atlas image
    atlas_size = atlas.GetSize()

    # Set the interpolation method
    interpolator = sitk.sitkLinear

    # Resample the image
    # Create a resampling filter
    resampling_filter = sitk.ResampleImageFilter()

    # Set the output size and interpolation method
    resampling_filter.SetSize(atlas_size)
    resampling_filter.SetInterpolator(interpolator)

    # Resample the image
    downsampled_image = resampling_filter.Execute(image)

    # Save the downsampled image
    sitk.WriteImage(downsampled_image, "downsampled_image.tif")

    return downsampled_image
