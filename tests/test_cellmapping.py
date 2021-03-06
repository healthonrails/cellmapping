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
    """Test filtering with the DoG filter"""
    from cellmapping.detect import filter_dog
    blobs = filter_dog(galaxy_image, min_sigma=1, max_sigma=5, threshold=.1)
    assert len(blobs) > 0


def test_remove_background(galaxy_image):
    """Test background remove from an image"""
    from cellmapping.detect import remove_background
    image_bg_removed = remove_background(galaxy_image)
    assert image_bg_removed.shape == galaxy_image.shape


def test_h_max_transform(galaxy_image, h_max=None):
    """Test H-max transformation of an image"""
    from cellmapping.detect import h_max_transform
    image_h_max = h_max_transform(galaxy_image, h_max=4.0)
    assert image_h_max.shape == galaxy_image.shape


def test_find_maxima(galaxy_image):
    """Test finding maxima in an image"""
    from cellmapping.detect import find_maxima
    image_max = find_maxima(galaxy_image, size=5, h_max=4)
    assert image_max.shape == galaxy_image.shape
