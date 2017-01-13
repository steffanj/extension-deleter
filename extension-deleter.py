from os import listdir
import os
'''
This is a script that can be used to delete files with a certain extension, 
given that a file with the same file name but with a different extension exists
in the same folder. It was initially created to delete those .JPG photos for 
which a more informative, "RAW" format .ORF file was available. In that 
application, it mainly served as an extra automated check to make sure that no 
.JPG files were deleted for which, because of some reason (e.g. an accidental 
delete or faulty camera settings), no RAW files existed anymore. 

How to use: 
In the code, specify the folder that contains the files that you would like to 
check. The folder should not contain any sub folders. The script will ask you 
for the file extensions that you like to use, which you should specify the 
extensions in the correct capitalization, i.e. in upper case (JPG) or lower 
case (jpg). The script will show which and how many files exist in both file 
types, and will ask you to confirm deletion of the 'inferior' files. 
    
To do: 
    * Make it possible to specify the folder without having to change the code
    * Make it possible to check files in one folder against files in another 
      folder
    * Make the script work in folders that contain sub folders
    * Make the script work with both lower and upper case representations of 
      the same extension (e.g. .JPG and .jpg should be checked both)
'''

# Path that possibly has files with the same name but different extensions
path = "C:/Users/ABC/XYZ/"

# Ask for the extension of the files that you would like to see deleted
delExt = input('Which extension do the files have that you would like to see '
               'deleted?\nPlease specify without a dot, e.g. "JPG": ')
prefExt = input('Which extension do the files have that you prefer over the '
               '.{} files?\nPlease specify without a dot, e.g. "PSD": '
               .format(delExt))

# Gather all files that are present in the folder
allfiles = listdir(path)

# Initiate and fill a list of those files that in principle you would like to 
# see deleted
delList = []
for i in allfiles:
	if i.split('.')[1] == delExt:
		delList.append(i.split('.')[0])

# Initiate and fill a list of those files that you prefer over the other files
prefList = []
for j in delList:
	if os.path.isfile(path+"\{}.{}".format(j,prefExt)):
		print('Preferred {} file present for {}.{}'.format(prefExt,j,delExt))
		prefList.append(j)

# Ask if the used indeed wants to delete the files for which a superior 
# alternative is present
if input('Do you want to delete the {} {} files for which a {} alternative exists'
         '? y/n: '.format(len(prefList), delExt, prefExt)) == 'y':
	for k in prefList:
		os.remove(path+"\{}.{}".format(k,delExt))
		print('Deleted {}.{}...'.format(k,delExt))
	print('Deleted {} {} files in total'.format(len(prefList), delExt))
else:
	print('Did not delete the {} files'.format(delExt))