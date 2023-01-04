import numpy as np
import pytest
from cellmapping.illumination_correction import correct_illumination

# Fixture to create test images


@pytest.fixture
def test_images():
    # Create a test image with uniform illumination
    image1 = np.ones((10, 10))

    # Create a test image with vignetting
    image2 = np.ones((10, 10))
    image2[:5, :5] = 0.5
    image2[5:, 5:] = 0.5

    return image1, image2


def test_correct_illumination(test_images):
    image1, image2 = test_images

    # Correct the images
    corrected_image1, corrected_image2 = correct_illumination(image1, image2)

    # Check that the correction function was applied correctly
    assert np.abs(np.mean(corrected_image1) - 1) < 1
    assert np.abs(np.mean(corrected_image2) - 1) < 1

    # Check that the vignetting has been corrected
    assert np.abs(np.mean(corrected_image2[:5, :5]) - 1) < 1
    assert np.abs(np.mean(corrected_image2[5:, 5:]) - 1) < 1
