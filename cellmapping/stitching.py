import numpy as np


def vertical_stack_images(img_t, img_b, end_t=160, start_b=840):
    """Stack images vertically with the given shift in y direction 
    assume img_t.shape == img_b.shape (z, y, x)

    Args:
        img_t (ndarray): image stack for top of the brain
        img_b (ndarray): image stack for bottom of the brain
        end_t (int, optional): end value in y direction for top section. Defaults to 160.
        start_b (int, optional): start value in y direction for bottom section. Defaults to 840.

    Returns:
        ndarray: combined image with img_t on top of img_b
    """
    img_combined = np.zeros(
        (img_t.shape[0],
          end_t+img_b.shape[1]- start_b,
         img_t.shape[2]))
    img_combined[:, :end_t, :] = img_t[:, :end_t, :]
    img_combined[:, end_t:, :] = img_b[:, start_b:, :]
    return img_combined
