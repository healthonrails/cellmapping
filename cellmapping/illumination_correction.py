import numpy as np
from skimage.feature import register_translation


def correct_illumination(image1, image2):
    # Align the images using phase cross-correlation
    shift, error, diffphase = register_translation(image1, image2)
    image2_aligned = np.roll(image2, shift, (0, 1))

    # Subtract the aligned image from the original image to get the difference image
    difference_image = image1 - image2_aligned

    # Compute the correction function from the difference image
    correction_function = np.median(difference_image)

    # Correct the original images by subtracting the correction function
    corrected_image1 = image1 - correction_function
    corrected_image2 = image2 - correction_function

    return corrected_image1, corrected_image2
