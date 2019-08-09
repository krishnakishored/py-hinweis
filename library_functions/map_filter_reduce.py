
items = [1,2,3,4,5,6]
squared = [x**2 for x in items ] # list comprehension

# The map call is similar to the list comprehension expression.
# But map applies a function call to each item instead of an arbitrary expression. 
# Because of this limitation, it is somewhat less general tool. 
# In some cases, however, map may be faster to run than a list comprehension such as when mapping a built-in function


def square(x):
        return (x**2)

def cube(x):
    return x**3


# map(aFunction, aSequence)     
cubed = list(map(cube,items))

# Because map expects a function to be passed in, 
# ßit also happens to be one of the places where lambda routinely appears:
doubled = list(map((lambda x:x*2),items))



# https://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php


from operator import add
from itertools import zip_longest
from functools import reduce


if __name__=="__main__":
    print(squared)
    print(cubed)
    print(doubled)

    #we can have a list of functions as aSequence:
    funcs=[square,cube]
    for r in range(5):
        value = map(lambda x:x(r),funcs)
        print(list(value)) 

    # given multiple sequence arguments, it sends items taken form sequences in parallel as distinct arguments to the function 
    print(list(map(pow,[2,3,4],[10,11,12])))   

    x = [1,2,3]
    y = [4,5,6]

    print(list(map(add,x,y))) # element wise addition

    for i,j in zip_longest(x,y):
        print(i,j) #The zip_longest() makes an iterator that aggregates elements from the two iterables (m & n).

    # Filter extracts each element in the sequence for which the function returns True. 
    # This Reduce function reduces a list to a single value by combining elements via a supplied function.

    print(list(range(-3,3)))
    print(list(filter((lambda x:x<0),range(-3,3))))

    #filter(): finding intersection of two lists:
    a = [1,2,3,5,7,9]
    b = [2,3,5,6,7,8]
    print(list(filter(lambda x: x in a, b)))  # prints out [2, 3, 5, 7]
    print([x for x in a if x not in b]) # [1, 9]  


    #reduce

    print(reduce( (lambda x, y: x * y), [1, 2, 3, 4] )) #24
    L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
    print(reduce( (lambda x,y:x+y), L))
    print("".join(L))
    print(reduce(add,L))#using the operator
    #The built-in reduce also allows an optional third argument placed before the items in the sequence to serve as a default result when the sequence is empty.

