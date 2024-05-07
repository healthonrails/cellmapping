import vtk
import numpy as np
from tifffile import TiffFile
import argparse


def convert_tiff_to_vtu(tiff_file, vtu_file):
    # Read the TIFF file
    with TiffFile(tiff_file) as tif:
        image_data = tif.asarray()

    # Create a VTK image data
    image_vtk = vtk.vtkImageData()
    image_vtk.SetDimensions(
        image_data.shape[2], image_data.shape[1], image_data.shape[0])
    image_vtk.AllocateScalars(vtk.VTK_UNSIGNED_SHORT, 1)

    # Convert the NumPy array to a contiguous memory block
    contiguous_data = np.ascontiguousarray(
        image_data.flatten(), dtype=np.uint16)

    # Convert the contiguous data to a VTK array
    vtk_array = vtk.vtkUnsignedShortArray()
    vtk_array.SetNumberOfComponents(1)
    vtk_array.SetNumberOfTuples(image_data.size)
    vtk_array.SetVoidArray(contiguous_data, image_data.size, 1)

    # Set the scalars for the image data
    image_vtk.GetPointData().SetScalars(vtk_array)

    # Write the VTU file
    writer = vtk.vtkXMLImageDataWriter()
    writer.SetFileName(vtu_file)
    writer.SetInputData(image_vtk)
    writer.Write()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert TIFF to VTU')
    parser.add_argument('tiff_file', help='Input TIFF file')
    parser.add_argument('vtu_file', help='Output VTU file')
    args = parser.parse_args()
    convert_tiff_to_vtu(args.tiff_file, args.vtu_file)
