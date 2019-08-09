# __name__ (name of the function),
# __doc__ (the docstring) and
# __module__ (The module in which the function is defined)
# of the original functions will be lost after the decoration. 

from greeting_decorator import greeting, greeting_manually, greeting_wraps

# @greeting
def f(x):
    """ just some silly function """
    return x + 4

@greeting_manually
def g(x):
    """ just some silly function """
    return x + 33


@greeting_wraps
def h(x):
    """ just some silly function """
    return x + 100    

if __name__=="__main__":
    print(f(10))
    print("function name: " + f.__name__)
    print("docstring: " + f.__doc__)
    print("module name: " + f.__module__)

    f = greeting(f)#after decorating
    print("function name: " + f.__name__)
    print("docstring: " + f.__doc__)
    print("module name: " + f.__module__)


    print(g(30))
    print("function name: " + g.__name__)
    print("docstring: " + g.__doc__)
    print("module name: " + g.__module__)



    print(h(19))
    print("function name: " + h.__name__)
    print("docstring: " + h.__doc__)
    print("module name: " + h.__module__)
