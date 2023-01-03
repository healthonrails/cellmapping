import os
import SimpleITK as sitk


def register_brain(half_brain_path, atlas_path):
    """This function will perform intensity-based registration
     of the half mouse brain image
     to the Allen Brain Atlas using the Advanced Mattes Mutual Information metric 
     and an affine transformation. The registered image will be saved as a TIFF file 
     with a unique name, and the path to the registered image will be returned by 
     the function.

    Args:
        half_brain_path (str): path for half mouse brain
        atlas_path (str): path for the atlas

    Returns:
        str: the path for the registered image
    """
    # Load the half mouse brain image
    half_mouse_brain = sitk.ReadImage(half_brain_path)

    # Load the Allen Brain Atlas
    allen_brain_atlas = sitk.ReadImage(atlas_path)

    # Set the parameters for the registration process
    parameter_map = {
        "MaximumNumberOfIterations": [100],
        "Metric": ["AdvancedMattesMutualInformation"],
        "Metric0Weight": [1.0],
        "Metric1Weight": [0.0],
        "Metric2Weight": [0.0],
        "Transform": ["AffineTransform"],
        "Transform0Weight": [1.0],
        "Transform1Weight": [0.0],
        "Transform2Weight": [0.0]
    }

    # Create an ElastixImageFilter object
    registration_method = sitk.ElastixImageFilter()

    # Set the fixed and moving images
    registration_method.SetFixedImage(allen_brain_atlas)
    registration_method.SetMovingImage(half_mouse_brain)

    # Set the parameter map
    registration_method.SetParameterMap(parameter_map)

    # Execute the registration
    registration_method.Execute()

    # Get the result of the registration
    registered_image = registration_method.GetResultImage()

    # Generate a unique output path for the registered image
    registered_image_path = os.path.splitext(
        half_brain_path)[0] + "_registered.tif"

    # Save the registered image
    sitk.WriteImage(registered_image, registered_image_path)

    # Return the path to the registered image
    return registered_image_path
