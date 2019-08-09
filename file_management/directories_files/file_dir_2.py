'''
https://realpython.com/working-with-files-in-python/


# https://realpython.com/read-write-files-python/#working-with-two-files-at-the-same-time

'''

import os
###############################################################################
## Traversing Directories and Processing Files

os.walk() is used to generate filename in a directory tree by walking the tree either top-down or bottom-up. 

os.walk() returns three values on each iteration of the loop:
- The name of the current folder
- A list of folders in the current folder
- A list of files in the current folder


for dirpath,dirnames,files in os.walk('my_directory'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)


To traverse the directory tree in a bottom-up manner, pass in a topdown=False keyword argument to os.walk():
for dirpath, dirnames, files in os.walk('my_directory', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)

###############################################################################
## Making Temporary Files and Directories

# from tempfile import TemporaryFile, NamedTemporaryFile
# # Create a temporary file and write some data to it
# fp = TemporaryFile('w+t') # This will create and open a file that can be used as a temporary storage area.


# # # If you need to name the temporary files produced using tempfile, use tempfile.NamedTemporaryFile().
# # fp = NamedTemporaryFile('w+t')
# # print(fp.name) #  /var/folders/mg/ydsfnrks3ls101ljhlc85ng00000gp/T/tmp7gk_ojy3

# fp.write('Hello universe!')

# # Go back to the beginning and read data from file
# fp.seek(0)
# data = fp.read()
# print(data)

# # Close the file, after which it will be removed
# fp.close()

###############################################################################
# Copying, Moving, and Renaming Files and Directories

# Python ships with the shutil module. shutil is short for shell utilities.

# import shutil

# # Copying Directories & files

# # src_dir = 'my_directory/my_child_dir1/'
# # dst_dir = 'my_directory/temp/'
# # shutil.copytree(src_dir, dst_dir)

# # src = 'my_directory/sample1.cpp'
# # dst = 'my_directory/temp/'
# # shutil.copy(src,dst)

# # Moving Directories & files
# # shutil.move('dir_1/', 'backup/')


# # Python includes os.rename(src, dst) for renaming files and directories:
# from pathlib import Path
# data_file = Path('data.txt')
# data_file.rename('data_01.txt')

###############################################################################

# Reading Multiple Files
# Python supports reading data from multiple input streams or from a list of files through the fileinput module. This module allows you to loop over the contents of one or more text files quickly and easily. 
import fileinput
import sys


files = fileinput.input()
for line in files:
    if fileinput.isfirstline():
        print(f'\n--- Reading {fileinput.filename()} ---')
    print(' -> ' + line, end='')
print()