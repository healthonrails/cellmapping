import argparse
import os
import numpy as np
import tifffile as tiff
from scipy.ndimage import zoom
from brainglobe_utils.IO.image import load_any

# List of olfactory-related region labels/IDs based on provided list
olfactory_region_ids = [
    416,  # Piriform area (PIR)
    390,  # Anterior olfactory nucleus (AON)
    379,  # Olfactory areas (OLF)
    380,  # Main olfactory bulb (MOB)
    386,  # Accessory olfactory bulb (AOB)
    387,  # Accessory olfactory bulb, glomerular layer (AOBgl)
    388,  # Accessory olfactory bulb, granular layer (AOBgr)
    389,  # Accessory olfactory bulb, mitral layer (AOBmi)
    421,  # Nucleus of the lateral olfactory tract (NLOT)
    423,  # Nucleus of the lateral olfactory tract, molecular layer (NLOT1)
    424,  # Nucleus of the lateral olfactory tract, pyramidal layer (NLOT2)
    425,  # Nucleus of the lateral olfactory tract, layer 3 (NLOT3)
    426,  # Cortical amygdalar area,(COA)
]


def filter_annotations(annotation, regions):
    """
    Filter the annotation data for the specified brain regions.

    Parameters:
    - annotation: numpy array, the annotation data.
    - regions: list of int, the brain region labels to filter.

    Returns:
    - filtered_annotation: numpy array, the filtered annotation data.
    """
    filtered_annotation = np.isin(
        annotation, regions).astype(np.uint16) * annotation
    return filtered_annotation


def rescale_annotation_to_brain(annotation_path, brain_path, regions, output_path=None):
    """
    Rescale the annotation TIFF file to match the size of the mouse brain TIFF file.

    Parameters:
    - annotation_path: str, path to the annotation TIFF file.
    - brain_path: str, path to the mouse brain TIFF file.
    - regions: list of int, brain region labels to filter.
    - output_path: str, optional, path to save the rescaled annotation TIFF file.

    Returns:
    - scaling_factors: tuple, the scaling factors used (x, y, z).
    """
    # Load the TIFF files
    annotation = tiff.imread(annotation_path)
    brain = tiff.imread(brain_path)

    # Filter the annotations
    annotation = filter_annotations(annotation, regions)

    # Get dimensions of the images
    annotation_shape = annotation.shape
    print("Annotation Shape:", annotation_shape)
    print("Annotation dtype", annotation.dtype)
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
                                   z_scaling_factor).astype(np.uint16)

    # Determine the output path if not provided
    if output_path is None:
        anno_dir = os.path.dirname(annotation_path)
        anno_basename = os.path.basename(annotation_path)
        output_path = os.path.join(
            anno_dir, f"{os.path.splitext(anno_basename)[0]}_filtered_rescaled.tif")

    # Save the rescaled annotation image
    tiff.imwrite(output_path, rescaled_annotation)
    print("Rescaled Annotation Shape:", rescaled_annotation.shape)

    return (x_scaling_factor, y_scaling_factor, z_scaling_factor)


def main():
    parser = argparse.ArgumentParser(
        description="Rescale an annotation TIFF file to match the size of a mouse brain TIFF file and filter for specified brain regions.")
    parser.add_argument("annotation_path", type=str,
                        help="Path to the annotation TIFF file.")
    parser.add_argument("brain_path", type=str,
                        help="Path to the mouse brain TIFF file.")
    parser.add_argument("--regions", type=int, nargs='+',
                        default=olfactory_region_ids, help="List of brain region labels to filter.")
    parser.add_argument("--output_path", type=str, default=None,
                        help="Path to save the rescaled annotation TIFF file (optional).")

    args = parser.parse_args()

    scaling_factors = rescale_annotation_to_brain(
        args.annotation_path, args.brain_path, args.regions, args.output_path)
    print("Scaling factors (x, y, z):", scaling_factors)


if __name__ == "__main__":
    main()
