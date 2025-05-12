'''
# https://realpython.com/working-with-files-in-python/
'''
###############################################################################
# Reading and writing 

# with open('data.txt','w')  as f:
#     data = 'some data to be written to the file'
#     f.write(data)
    
# with open('data.txt','r') as f:
#     data = f.read() # some data to be written to the file
#     # data = f.readline()
#     # data = f.readlines() # ['some data to be written to the file']
#     print(data)
###############################################################################
# Getting a Directory Listing
# The built-in os module has a number of useful functions that can be used to list directory contents and filter the results. 
# import os 

# os.listdir() returns a Python list containing the names of the files and subdirectories in the directory given by the path argument:
# entries = os.listdir('my_directory')

# # os.scandir() was introduced in Python 3.5 and is documented in PEP 471. os.scandir() returns an iterator as opposed to a list when called:
# entries = os.scandir('my_directory')
# print(entries) #<posix.ScandirIterator object at 0x10199f578>
# for entry in entries:
#     print(entry.name)


# # Another way to get a directory listing is to use the pathlib module:
# # The objects returned by Path are either PosixPath or WindowsPath objects depending on the OS.
# # pathlib.Path() objects have an .iterdir() method for creating an iterator of all files and folders in a directory. 
# # Each entry yielded by .iterdir() contains information about the file or directory such as its name and file attributes.
# from pathlib import Path
# entries = Path('my_directory')
# for entry in entries.iterdir():
#     print(entry.name)


# # Using pathlib.Path() or os.scandir() instead of os.listdir() is the preferred way of getting a directory listing, 
# # especially when you’re working with code that needs the file type and file attribute info 

## Listing All Files in a Directory

# basepath = 'my_directory'
# with os.scandir(basepath) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(entry.name)

# # List all files in directory using pathlib
# from pathlib import Path
# basepath = Path('my_directory')
# files_in_basepath = basepath.iterdir()
# for item in files_in_basepath:
#     if item.is_file():
#         print(item.name)

# # using generator expressions
# # List all files in directory using pathlib
# files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
# for item in files_in_basepath:
#     print(item.name)


# # Listing Subdirectories
# directories_in_basepath = (directory for directory in basepath.iterdir() if directory.is_dir())
# for item in directories_in_basepath:
#     print(item.name)

###############################################################################
# Getting File Attributes


###############################################################################
# Filename Pattern Matching Using glob

# import glob
# print(glob.glob('*.py', recursive=True))


from pathlib import Path
p = Path('my_directory')

# cpp_files = p.glob('*.cpp') # in the Path dir
cpp_files = p.glob('**/*.cpp') # recursively in the sub directories
print(cpp_files) # <generator object Path.glob at 0x10bad5750>
for file in cpp_files:
    print(file)

###############################################################################


