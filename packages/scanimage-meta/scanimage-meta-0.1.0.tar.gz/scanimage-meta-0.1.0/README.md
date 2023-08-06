Nicer metadata format wrapper for scanimage tif reader:
https://pypi.org/project/scanimage-tiff-reader/

Provides more convenient and object oriented access 

Current status: 
    Works, but not thouroughly tested 



Example:

meta = ScanimageMeta.fromfilepath('scanimagetif.tif')
print(meta.SI.hRoiManger.scanFrameRate)
