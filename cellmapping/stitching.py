import numpy as np


def vertical_stack_images(img_t, img_b, shift_t=160, shift_b=840):
    """Stack images vertically with the given shift in y direction 
    assume img_t.shape == img_b.shape (z, y, x)

    Args:
        img_t (ndarray): image stack for top of the brain
        img_b (ndarray): image stack for bottom of the brain
        shift_t (int, optional): shift value in y direction. Defaults to 160.
        shift_b (int, optional): shift value in y direction. Defaults to 840.

    Returns:
        ndarray: combined image with img_t on top of img_b
    """
    img_combined = np.zeros(
        (img_t.shape[0],
         img_t.shape[1]-shift_t+img_b.shape[1]-shift_b,
         img_t.shape[2]))
    img_combined[:, :img_t.shape[1], :] = img_t
    img_combined[:, img_t.shape[1]-shift_t:, :] = img_b[:, shift_b:, :]
    return img_combined
