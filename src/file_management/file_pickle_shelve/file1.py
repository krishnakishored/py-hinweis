'''
https://www.python-course.eu/python3_file_management.php

'''
####################################################################


# fobj = open("tworoads.txt","r") # "r" is optional

# for line in fobj:
#     print(line.rstrip())
# fobj.close()

# fh = open("example.txt", "w")
# fh.write("To write or not to write\nthat is the question!\n")
# fh.close()

####################################################################

# # You will often find the 'with' statement for reading and writing files. The advantage is that the file will be automatically closed after the indented block after the with has finished execution
# with open("tworoads.txt","r") as fobj:
#     for line in fobj:
#         print(line.rstrip())
#         print(line)

####################################################################

# # simultaneous read-write
# fobj_in = open("tworoads.txt")
# fobj_out = open("copy.txt","a") # append
# i = 1
# for line in fobj_in:
#     print(line.rstrip())
#     fobj_out.write(str(i) + ": " + line)
#     i = i + 1
# fobj_in.close()
# fobj_out.close()

####################################################################

# Reading in one go

# poem = open("tworoads.txt").readlines()
# # print(poem)
# print(poem[10:16])

####################################################################

# # Resetting the Files Current Position
# fh = open("tworoads.txt")
# print(fh.tell())
# fh.read(18)
# print(fh.tell())#18
# print(fh.read())
# print(fh.tell())#731
# print(fh.seek(9)) # 9
# print(fh.read(15)) # diverged in a
####################################################################
# # It's also possible to set the file position relative to the current position by using tell correspondingly:
# fh = open("tworoads.txt")
# print(fh.read(18)) # Two roads diverged
# print(fh.seek(fh.tell() - 8))
# print(fh.read(18)) #diverged in a yell
# fh.seek(fh.tell() + 29)
# print(fh.read(13)) #t travel both

####################################################################
# # Read and Write to the Same File

# In the following example we will open a file for reading and writing at the same time. 
# If the file doesn't exist, it will be created. If you want to open an existing file for read and write, 
# you should better use "r+", because this will not delete the content of the file.


# fh = open('colours.txt', 'w+')
# fh.write('The colour brown')

# # Go to the 12th byte in the file, counting starts with 0
# fh.seek(11)   
# print(fh.read(5))#brown
# print(fh.tell())#16
# fh.seek(11)
# fh.write('green')
# fh.seek(0)
# content = fh.read()
# print(content) #The colour green

####################################################################
# "How to get into a Pickle"
# With the algorithms of the pickle module we can serialize and de-serialize Python object structures

# Objects which have been dumped to a file with pickle.dump can be reread into a program by using the method pickle.load(file). pickle.load recognizes automatically, which format had been used for writing the data. 

# import pickle
# cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
# fh = open("data.pkl", "bw")
# pickle.dump(cities, fh)
# fh.close()


# # The file data.pkl can be read in again by Python in the same or another session or by a different program:
# f = open("data.pkl", "rb")
# villes = pickle.load(f)
# print(villes) # ['Paris', 'Dijon', 'Lyon', 'Strasbourg']
# # Only the objects and not their names are saved. That's why we use the assignment to villes in the previous example, i.e. data = pickle.load(f). 



# # Pickling multiple objects
# # We pack the objects into another object, so we will only have to pickle one object again

# fh = open("data.pkl","bw")
# programming_languages = ["Python", "Perl", "C++", "Java", "Lisp"]
# python_dialects = ["Jython", "IronPython", "CPython"]
# pickle_object = (programming_languages, python_dialects)
# pickle.dump(pickle_object,fh)
# fh.close()

# f = open("data.pkl","rb")
# (languages, dialects) = pickle.load(f)
# print(languages, dialects)
# # ['Python', 'Perl', 'C++', 'Java', 'Lisp'] ['Jython', 'IronPython', 'CPython']

####################################################################
# Shelve Module
import shelve
# s = shelve.open("MyShelve")

# If the file "MyShelve" already exists, the open method will try to open it. 
# If it isn't a shelf file, - i.e. a file which has been created with the shelve module,
# we will get an error message. If the file doesn't exist, it will be created. 



# s["street"] = "Fleet Str"
# s["city"] = "London"
# for key in s:
#     print(key)
# s.close()

# # We can use the previously created shelf file in another program or in an interactive Python session: 
# print(s["street"]) # Fleet Str

# # It is also possible to cast a shelf object into an "ordinary" dictionary with the dict function: 
# print(s) #<shelve.DbfilenameShelf object at 0x107ce6048>
# t = dict(s)
# print(t) # {'street': 'Fleet Str', 'city': 'London'}

# tele = shelve.open("MyPhoneBook")
# tele["Mike"] = {"first":"Mike", "last":"Miller", "phone":"4689"}
# tele["Steve"] = {"first":"Stephan", "last":"Burns", "phone":"8745"}
# tele["Eve"] = {"first":"Eve", "last":"Naomi", "phone":"9069"}
# print(tele["Eve"]["phone"]) # 9069

# shelve.close() 
# # but the data is persistent


# tele = shelve.open("MyPhoneBook")
# print(tele["Steve"]["phone"]) # 8745

####################################################################


# The file cities_and_times.txt contains city names and times. 
# Each line contains the name of the city, followed by the name of the day ("Sun") and the time in the form hh:mm. 
# Read in the file and create an alphabetically ordered list of the form
# [('Amsterdam', 'Sun', (8, 52)), ('Anchorage', 'Sat', (23, 52)), ('Ankara', 'Sun', (10, 52)), ('Athens', 'Sun', (9, 52)), ('Atlanta', 'Sun', (2, 52)), ('Auckland', 'Sun', (20, 52)), ('Barcelona', 'Sun', (8, 52)), ('Beirut', 'Sun', (9, 52)), 

import pickle

lines = open("cities_and_times.txt").readlines()
lines.sort()

cities = []

for line in lines:
    *city,day,time = line.split()
    hours, minutes = time.split(":")
    cities.append((" ".join(city),day,(int(hours),int(minutes))))
    # cities.append((" ".join(city), day, (int(hours), int(minutes)) ))
fh = open("cities_and_times.pkl","bw")    
pickle.dump(cities,fh)
fh.close()

# now it's persistent

fh = open("cities_and_times.pkl","rb")    
mycities =  pickle.load(fh)
print(mycities[0]) #('Amsterdam', 'Sun', (8, 52))
fh.close()





####################################################################