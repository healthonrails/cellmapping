// Cell Detection
// Mapping the detected cells to Atlas space

// init 
run("Clear Results"); 
run("Close All");
run("ROI Manager...");

setBatchMode(true);

#@ String (visibility=MESSAGE, value="<html><h1><font size=7 color=#B31B1B>Cell Mapping Pipeline</h><br/><h3><font size = 5><a href=https://cplab.net//> Cell Mapping Pipeline</a></html>") doc

  
#@ File(label="Select directory:", description="directory containing brain raw data", style="directory") input

#@ String(label="Expression raw:", value = "Ex_647_Em_690_stitched/053290_096610_<Z,6>.tif", style="listBox") ExpressionRaw
#@ String(label="Expression auto:",value = "Ex_488_Em_525_stitched/053290_096610_<Z,6>.tif", style="listBox") ExpressionAuto

#@ String(label="Brain orientation:", choices={"1,2,3", "1,-2,3", "3,2,1"}, style="listBox", description="The scan has the same orientation as the atlas reference: 1, 2, 3") Orientation


#@ Double(label="Auto (XY) resolution of input (um):", value = 1.8, style="spinner") InputResAutoXY
#@ Double(label="Auto (Z) resolution of input (um):", value = 4.0, style="spinner") InputResAutoZ

#@ Double(label="Expression raw (XY) resolution of input (um):", value = 1.8, style="spinner") InputResRawXY
#@ Double(label="Expression raw (Z) resolution of input (um):", value = 4.0, style="spinner") InputResRawZ



#@ Double(label="Atlas resolution(um):", value = 25, description="Atlas  resolution", style="spinner") AtlasResolution

#@String  (visibility="MESSAGE", value="------------------------------------Cell Detection and Analysis ----------------------------------------") out2
#@ String(label="Method for cell detection:", choices={"Find Maxima", "Machine Learning Segmentation with Ilastik"}, value = "Machine Learning Segmentation with Ilastik", style="listBox", description="") CellDetType

#@ Integer(label="Minimum intensity threshold:", value = 125, style="spinner") MaximaInt1
#@ Integer(label="Minimum cell area (um):", value = 20, style="spinner") Size1

#@ File(label="Ilastik location (if using Ilastik for segmentation):", value = "/usr/local/ilastik-1.3.3post1", style="directory") IlastikDir
ilastik = IlastikDir + "/run-ilastik.sh";

title1 = "Brain Image Parameters"; 
title2 = "["+title1+"]"; 
f=title2; 
run("New... ", "name="+title2+" type=Table"); 
print(f,"\\Headings:Parameter\tValue");

	
print(f,"Directory:\t"+input); //0
print(f,"Expression raw:\t"+ExpressionRaw); //1
print(f,"Expression auto:\t"+ExpressionAuto); //2



print(f,"Brain orientation:\t"+Orientation); //3

print(f,"Auto (XY) resolution of input (um):\t"+InputResAutoXY); //4
print(f,"Auto (Z) resolution of input (um):\t"+InputResAutoZ); //5

print(f,"Expression raw (XY) resolution of input (um):\t"+InputResRawXY); //6
print(f,"Expression raw (Z) resolution of input (um):\t"+InputResRawZ); //7



print(f,"Atlas resolution(um):\t"+AtlasResolution); //8

	
selectWindow(title1);	
saveAs("txt", input + "/Brain_Image_Parameters.csv");
closeWindow(title1);

// run a bash script for the background tasks
// e.g.
// exec("sh","/home/annolid/run_annolid.sh");

function closeWindow(windowname) {
	if (isOpen(windowname)) { 
      		 selectWindow(windowname); 
       		run("Close"); 
  		} 
}
