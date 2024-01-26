# cellmapping


Mouse Brain Image Registration and Cell Detection
This repository contains code for registering mouse brain images to an atlas and detecting and counting cells in different regions of the brain.

# Requirements
To use the code in this repository, you will need to have the following software and libraries installed on your computer:
```
Python 3
SimpleITK
scikit-image
NumPy
SciPy
```
Create an conda env for brainglobe
```
conda create -n brainglobe python==3.10
pip install -r requirements.txt 
# pip install brainglobe-workflows
```
Note: If you encounter the following error message  <fatal error: 'H5public.h' file not found 
> on Mac, please try install dhf5 with
```
conda install hdf5
```.
You can install these dependencies by running the following command:

```
pip install SimpleITK scikit-image numpy scipy
```
# Usage
To register a mouse brain image to an atlas, use the register_brain function in the brain_registration.py module:
```
from brain_registration import register_brain

registered_image_path = register_brain("half_mouse_brain.tif", "allen_brain_atlas.tif")
```
This function will perform intensity-based registration of the mouse brain image to the atlas using the Advanced Mattes Mutual Information metric and an affine transformation. The registered image will be saved as a TIFF file with a unique name, and the path to the registered image will be returned by the function.

To detect and count cells in different regions of the brain, use the detect_cells function in the cell_detection.py module:
```
from cell_detection import detect_cells

cell_counts = detect_cells("registered_mouse_brain.tif")
```
This function will detect cells in the registered mouse brain image using a combination of thresholding, morphological operations, and blob detection. It will then count the cells in each region of the brain and return a dictionary of cell counts.

To register brain atlas to a sample brain, here is one example for using brainreg
```ome/
brainreg /path/to/auto_background.tif /path/to/outputs -v 20 5 5 --orientation ras --brain_geometry hemisphere_r

```
Note:  for -v or --voxel-sizes  flags
The unit is micron. The first value is plane spacing i.e. the z-depth is 20 microns and the in-plane resolution is 5x5 microns. 

For --orientation, the string is in bg-space initials form as the axis order(sliced plane, height, width).
Horizontal section
If the first plane of this image was the top of the brain it would be sal/sar. If the first plane was the base it would be ial/iar.

Coronal section
If the first plane of this image was olfactory bulb, it would be asr (or asl). If the first plane was cerebellum, it would be psr or psl.
https://brainglobe.info/documentation/general/image-definition.html

# License
The code in this repository is released under the MIT License. 
Acknowledgments
