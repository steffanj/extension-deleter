# extension-deleter
A script that can be used to delete files with a certain extension if the same file exists in a preferred file format.

## Description
This is a script that can be used to delete files with a certain extension, 
given that a file with the same file name but with a different extension exists
in the same folder. It was initially created to delete those .JPG photos for 
which a more informative, "RAW" format .ORF file was available. In that 
application, it mainly served as an extra automated check to make sure that no .JPG files 
were deleted for which, because of some reason (e.g. an accidental delete or 
faulty camera settings), no RAW files existed anymore. 

## How to use
Specify the folder that contains the files that you would like to check. The folder should not
contain any sub folders. The script will ask you for the file extensions that you like to use, 
which you should specify the extensions in the correct capitalization, i.e. in upper case (JPG) 
or lower case (jpg). The script will show which and how many files exist in both file types, 
and will ask you to confirm deletion of the 'inferior' files.  

## To do
- [ ] Make it possible to specify the folder without having to change the code
- [ ] Make it possible to check files in one folder against files in another folder
- [ ] Make the script work in folders that contain sub folders
- [ ] Make the script work with both lower and upper case representations of the same extension (e.g. .JPG and .jpg should be checked both)
