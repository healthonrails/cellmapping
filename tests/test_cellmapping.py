#!/usr/bin/env python

"""Tests for `cellmapping` package."""

import pytest


from cellmapping import cellmapping


@pytest.fixture
def galaxy_image():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    import skimage
    from skimage.color import rgb2gray
    image = skimage.data.hubble_deep_field()[0:500, 0:500]
    image_gray = rgb2gray(image)
    return image_gray


def test_filter_dog(galaxy_image):
    """Sample pytest test function with the pytest fixture as an argument."""
    from skimage.feature import blob_dog
    blobs = blob_dog(galaxy_image, min_sigma=1, max_sigma=5, threshold=.1)
    assert len(blobs) > 0
