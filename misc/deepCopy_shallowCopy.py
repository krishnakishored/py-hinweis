x = 3
y = x
print(id(x), id(y))
#1503920656 1503920656
y = 4
print(id(x), id(y))
#1503920656 1503920688
print(x,y)
#3 4
#Python creates only real copies, if it has to, i.e. if the user, the programmer, explicitly demands it.

#Copying a list

colours1 = ["red", "blue"]
colours2 = colours1

print(colours2)
print(id(colours1),id(colours2))
#['red', 'blue']
#45079752 45079752

colours2 = ["rouge", "vert"]
print(colours1)
print(colours2)
#['red', 'blue']
#['rouge', 'vert']

print(id(colours1),id(colours2))
#45079752 45115976

#Copy with the Slice Operatorl
print("Copy with the Slice Operator")
list1 = ['a','b','c','d']
list2 = list1[:]


print(id(list1),": ","list1 items:")
print(id(list2),": ","list2 items:")

for item1 in list1:
    print(id(item1)," ",end="")
print("----------------------------")
for item2 in list2:
    print(id(item2)," ",end="")
print("----------------------------")

list2[0]= 'z'
for item1 in list1:
    print(id(item1)," ",end="")
print("----------------------------")
for item2 in list2:
    print(id(item2)," ",end="")
print("----------------------------")

lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
for item1 in lst1:
    print(id(item1)," ",end="")
print("----------------------------")
for item2 in lst2:
    print(id(item2)," ",end="")
print("----------------------------")

print(lst1[2][1],"__",lst2[2][1])
lst2[2][1] = 'd'
# We can see that both lst1 and lst2 are affected by the assignment lst2[2][1] = 'd':
print(id(lst1[2][1]),": ","lst1[2][1] items:")
print(id(lst2[2][1]),": ","lst2[2][1] items:")
print(lst1[2][1],"__",lst2[2][1])

#Using the Method deepcopy from the Module copy
'''
A solution to the described problems provide the module "copy".
This module provides the method "deepcopy", which allows a complete or deep copy of an arbitrary list, i.e. shallow and other lists.
'''

from copy import deepcopy
lst2 = deepcopy(lst1)
print(id(lst1),": ","lst1 items:")
print(id(lst2),": ","lst2 items:")
