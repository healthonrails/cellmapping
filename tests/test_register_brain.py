import os
import unittest
import tiffile
import numpy as np
from cellmapping.register import register_brain


class TestRegisterBrains(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Generate a random NumPy array with shape (64, 64, 64)
        cls.image = np.random.random((64, 64, 64)).astype(np.float32)

        # Save the array as a TIFF file
        tiffile.imwrite("image.tif", cls.image)

        # Generate a random NumPy array with shape (64, 64, 64)
        cls.atlas = np.random.random((64, 64, 64)).astype(np.float32)

        # Save the array as a TIFF file
        tiffile.imwrite("atlas.tif", cls.atlas)

    def test_register_brains(self):
        # Test that the function correctly registers two brain images
        registered_image_path = register_brain("image.tif", "atlas.tif")
        self.assertTrue(os.path.exists(registered_image_path))

        # Test that the function correctly handles an invalid image1 path
        with self.assertRaises(RuntimeError):
            register_brain("invalid_image1.tif", "image2.tif")

        # Test that the function correctly handles an invalid image2 path
        with self.assertRaises(RuntimeError):
            register_brain("image1.tif", "invalid_image2.tif")


if __name__ == '__main__':
    unittest.main()
