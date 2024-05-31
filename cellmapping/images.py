import argparse
import os
import tifffile as tiff
from scipy.ndimage import zoom
from brainglobe_utils.IO.image import load_any


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
    print("Annotation Shape:", annotation_shape)
    brain_shape = brain.shape
    print("Brain Shape:", brain_shape)
    del brain

    # Calculate scaling factors
    x_scaling_factor = brain_shape[2] / annotation_shape[2]
    y_scaling_factor = brain_shape[1] / annotation_shape[1]
    z_scaling_factor = brain_shape[0] / annotation_shape[0]
    print("Scaling factors for x, y, z:", x_scaling_factor,
          y_scaling_factor, z_scaling_factor)

    # Apply zoom to rescale the annotation image
    rescaled_annotation = load_any(annotation_path,
                                   x_scaling_factor,
                                   y_scaling_factor,
                                   z_scaling_factor)

    # Determine the output path if not provided
    if output_path is None:
        anno_dir = os.path.dirname(annotation_path)
        anno_basename = os.path.basename(annotation_path)
        output_path = os.path.join(
            anno_dir, f"{os.path.splitext(anno_basename)[0]}_original_scale.tif")

    # Save the rescaled annotation image
    tiff.imwrite(output_path, rescaled_annotation.astype(annotation.dtype))
    print("resacle anno shape: ", rescaled_annotation.shape)

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
