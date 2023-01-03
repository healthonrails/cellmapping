import unittest
import tiffile
import numpy as np
from cellmapping.tif import downsample_image


class TestDownsampleImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Generate a random NumPy array with shape (128, 128, 128)
        cls.image = np.random.random((128, 128, 128)).astype(np.float32)

        # Save the array as a TIFF file
        tiffile.imwrite("image.tif", cls.image)

        # Generate a random NumPy array with shape (64, 64, 64)
        cls.atlas = np.random.random((64, 64, 64)).astype(np.float32)

        # Save the array as a TIFF file
        tiffile.imwrite("atlas.tif", cls.atlas)

    def test_downsample_image(self):
        # Test that the function correctly downsamples an image to the size of an atlas image
        downsampled_image = downsample_image("image.tif", "atlas.tif")
        self.assertEqual(downsampled_image.GetSize(), self.atlas.shape)

        # Test that the function correctly handles an invalid image path
        with self.assertRaises(RuntimeError):
            downsample_image("invalid_image.tif", "atlas.tif")

        # Test that the function correctly handles an invalid atlas path
        with self.assertRaises(RuntimeError):
            downsample_image("image.tif", "invalid_atlas.tif")


if __name__ == '__main__':
    unittest.main()
