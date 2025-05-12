# https://python-course.eu/python3_list_manipulation.php
# https://python-course.eu/python3_sequential_data_types.php

def accessing_list():
    languages = ["Python", "C", "C++", "Java", "Perl"]
    print(languages[-1]) # Perl
    complex_list = [["a",["b",["c","x"]]]]
    print(complex_list[0][1][1][0]) # c
    person = [["Marc","Mayer"],["17, Oxford Str", "12345","London"],"07876-7876"]
    print(person[1][0]) # 17, Oxford Str


    '''
    A tuple is an immutable list. 
    Once created, you can't add elements to a tuple or remove elements from a tuple. 
    Tuples are faster than lists.
    The main advantage of tuples consists in the fact that tuples can be used as keys in dictionaries, while lists can't.
    '''
    t = ("tuples", "are", "immutable")
    print(t[-1]) # immutable
    # t[0]="assignments to elements are not possible" # TypeError: 'tuple' object does not support item assignment
    print('#################################')

    '''
    slicing
    '''
    str = "Python is great"
    first_six = str[0:6]
    print(first_six) 
    without_last_five = str[0:-5]
    print(without_last_five) # Python is
    starting_at_five = str[5:]
    print(starting_at_five) # n is great

    '''
    Slicing works with three arguments as well. 
    s[begin: end: step]
    '''
    str = "Python under Linux is great"
    print(str[::3]) # Ph d n  e

    s = 'TPoyrtohnotno  ciosu rtshees  lianr gTeosrto nCtiot yb yi nB oCdaennasdeao'
    t1 = s[::2]
    t2 = s[1::2]
    print(t1)  # Toronto is the largest City in Canada
    print(t2) # Python courses in Toronto by Bodenseo
    
    s = "".join(["".join(x) for x in zip(t1,t2)])
    print(s) # use of list comprehension

    '''
    The augmented assignment "+=" which is well known for arithmetic assignments work for sequences as well.
    `s += t` is only syntactically same as `s = s + t`
    In the first case the left side has to be evaluated only once.
    Augment assignments may be applied for mutable objects as an optimization. 
    '''


    abc = ["a","b","c","d","e"]
    print("a" in abc) # True


    '''
    Repetitions
    str * 4 = str + str + str + str
    '''
    x = ["a","b","c"]
    y = [x] * 4 
    print(y) #  [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    y[0][0] = 'p'
    print(y) # [['p', 'b', 'c'], ['p', 'b', 'c'], ['p', 'b', 'c'], ['p', 'b', 'c']]
    '''
    The reason is that the repetition operator "* 4" creates 4 references to the list x: 
    and so it's clear that every element of y is changed, if we apply a new value to y[0][0]. 
    '''





def comparison_append_approaches():
    '''
    Comparison of approaches - append(), l=l+item, l+=item

    o/p
    15.066668033599854
    0.0160369873046875
    0.01364898681640625

    We can see that the "+" operator is about 1268 slower than the append method. 
    - the append method simply appends a further element to the list in each loop pass. 
    - l = l + [i * 2]. 
      The list will be copied in every loop pass. The new element will be added to the copy of the list and result will be reassigned to the variable l. 
      After this the old list will have to be removed by Python, because it is not referenced anymore. 
    - the augmented assignment ("+="), the loop in the middle, is only slightly slower than the version using "append".
    '''
    import time

    n= 100000

    start_time = time.time()
    l = []
    for i in range(n):
        l = l + [i * 2]
    print(time.time() - start_time)

    start_time = time.time()
    l = []
    for i in range(n):
        l += [i * 2]
    print(time.time() - start_time)

    start_time = time.time()
    l = []
    for i in range(n):
        l.append(i * 2)
    print(time.time() - start_time)

def basics_list():
    '''
    append(), pop(), extend(), +, remove(), index()
    '''

    lst = [21,34,56]
    lst.append(199)
    print(lst)
    lst.pop()
    print(lst)
    lst.pop(1)
    print(lst)
    lst2 = [99,33,55,66]
    lst.append(lst2) 
    print(lst)
    lst.extend(lst2) # [21, 56, [99, 33, 55, 66], 99, 33, 55, 66]
    print(lst)
    lst.pop(2)
    print(lst)
    '''
    The argument of extend doesn't have to be a list. 
    It can be any iterable. 
    This means that we can use tuples and strings as well
    '''
    lst = ["a", "b", "c"]
    prg_lang= "Python"
    lst.extend(prg_lang)
    print(lst) # ['a', 'b', 'c', 'P', 'y', 't', 'h', 'o', 'n']
    tup1 = ('C++','C#','Python','js')
    lst.extend(tup1)
    print(lst) # ['a', 'b', 'c', 'P', 'y', 't', 'h', 'o', 'n', 'C++', 'C#', 'Python', 'js']

    '''
    Extending and Appending Lists with the '+'-Operator
    '''
    print('#################################')
    level = ["beginner", "intermediate", "advanced"]
    other_words = ["novice", "expert"]
    combo = level+other_words
    print(combo)

    '''
    Removing an element with remove
    s.remove(x) removes x from a list without knowing the position.
    if x is not contained in the list, a ValueError is raised
    '''
    colours = ["red", "green", "blue", "green", "yellow"]
    colours.remove('blue') # ['red', 'green', 'green', 'yellow']
    print(colours)
    # colours.remove('blue') # ValueError: list.remove(x): x not in list
    
    '''
    Find the Position of an Element in a List

    s.index(x[, i[, j]])
    It returns the first index of the value x. 
    A ValueError will be raised, if the value is not present. 
    If the optional parameter i is given, the search will start at the index i. 
    If j is also given, the search will stop at position j.
    '''
    colours = ["red", "green", "blue", "green", "yellow"]
    # print(colours.index("green")) # 1
    # print(colours.index("green",2)) # 3 
    print(colours.index("green",2,4)) # 3


    '''
    s.insert(index, object)
    '''
    lst = ["German is spoken", "in Germany,", "Austria", "Switzerland"]
    lst.insert(3, "and")
    print(lst)
    # mimics append()
    lst.insert(len(lst),"India") # ['German is spoken', 'in Germany,', 'Austria', 'and', 'Switzerland', 'India']
    print(lst)

if __name__ == "__main__":
    # basics_list()
    # comparison_append_approaches()
    accessing_list()
    
    
    
    