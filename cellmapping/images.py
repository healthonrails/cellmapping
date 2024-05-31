import numpy as np
from scipy.ndimage import zoom
import tifffile as tiff
import argparse
import os


def rescale_annotation_to_brain(annotation_path, brain_path, output_path=None):
    """
    Rescale the annotation TIFF file to match the size of the mouse brain TIFF file.

    Parameters:
    - annotation_path: str, path to the annotation TIFF file.
    - brain_path: str, path to the mouse brain TIFF file.
    - output_path: str, optional, path to save the rescaled annotation TIFF file.

    Returns:
    - scaling_factors: tuple, the scaling factors used (x, y, z).
    """
    # Load the TIFF files
    annotation = tiff.imread(annotation_path)
    brain = tiff.imread(brain_path)

    # Get dimensions of the images
    annotation_shape = annotation.shape
    brain_shape = brain.shape

    # Calculate scaling factors
    x_scaling_factor = brain_shape[1] / annotation_shape[1]
    y_scaling_factor = brain_shape[0] / annotation_shape[0]
    z_scaling_factor = brain_shape[2] / annotation_shape[2]

    # Apply zoom to rescale the annotation image
    rescaled_annotation = zoom(annotation, (y_scaling_factor,
                                            x_scaling_factor,
                                            z_scaling_factor), order=3)

    # Determine the output path if not provided
    if output_path is None:
        brain_dir = os.path.dirname(brain_path)
        brain_basename = os.path.basename(brain_path)
        output_path = os.path.join(
            brain_dir, f"{os.path.splitext(brain_basename)[0]}_anno.tif")

    # Save the rescaled annotation image
    tiff.imwrite(output_path, rescaled_annotation.astype(annotation.dtype))

    return (x_scaling_factor, y_scaling_factor, z_scaling_factor)


def main():
    parser = argparse.ArgumentParser(
        description="Rescale an annotation TIFF file to match the size of a mouse brain TIFF file.")
    parser.add_argument("annotation_path", type=str,
                        help="Path to the annotation TIFF file.")
    parser.add_argument("brain_path", type=str,
                        help="Path to the mouse brain TIFF file.")
    parser.add_argument("--output_path", type=str, default=None,
                        help="Path to save the rescaled annotation TIFF file (optional).")

    args = parser.parse_args()

    scaling_factors = rescale_annotation_to_brain(
        args.annotation_path, args.brain_path, args.output_path)
    print("Scaling factors (x, y, z):", scaling_factors)


if __name__ == "__main__":
    main()
