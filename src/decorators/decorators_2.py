#Decorators can be used for different purposes some common one are shown below.

from argcheck import check
#1. We check if the positional arguments to a function call are of a certain type.
@check(int,int)
def add(x, y):
    """Add two integers."""
    return x + y

print(add.__doc__)
#add(1) #TypeError: Expected 2 but got 1 arguments
#add(1,'a') #TypeError: Expected (<class 'int'>, <class 'int'>) but got (<class 'int'>, <class 'str'>)

#We can't use our function if we have a different number of parameters in the decorator than in the function definition:

@check(int, int, int)
def add(x, y):
    """Add two integers."""
    return x + y

#add(1,2) #TypeError: Expected 3 but got 2 arguments


#2.Caching results with a decorator
from cached import cached

@cached
def add(a, b):
    print('calc')
    return a + b

print(add(10,10))
print(add(10,10))
print(add(10,10))



#3. LOGGING: We log things if the global variable LOGGING is true:
import logged

@logged.logged
def add(a, b):
    return a + b

logged.LOGGING = True
print(add(10,111))

#4. Registration
'''We would like to register functions. The first way is to make them append themselves to a list when they are called. We use a dictionary registry to store these lists.'''

from registering import registry, register_at_call

print(registry)

@register_at_call('simple')
def f1():
    pass

@register_at_call('simple')
def f2():
    pass

@register_at_call('complicated')
def f3():
    pass

print(registry)
f1()
f2()
f3()

print(registry)
names = [f.__name__ for f in registry['simple']]
print(names)
names2 = [f.__name__ for f in registry['complicated']]
print(names2)


#Of course we will append a function every time we call it:
f3()
f3()

print(registry)

#If want to register our function at definition time, we have to change our decorator:
from registering import register_at_def

registry2 = {}

@register_at_def('simple')
def f4():
    pass

print(registry2)
f4()
print(registry2)
'''
Calling doesn't change anything in the registry: ????
'''

#5. Verification is another useful way to use decorators.

def assert_fluid(cls):
    assert 0 <= cls.temperature <= 100
    return cls



@assert_fluid
class Water(object):
    temperature = 20

@assert_fluid
class Steam(object):
    temperature = 120 #AssertionError

@assert_fluid
class Ice(object):
    temperature = -20 #AssertionError

'''
Exercises
1. Write  a  function  decorator  that  can  be  used  to  measure  the  run  time  of  a  functions.  Use timeit.default_timer to get time stamps.
2. Make the decorator parameterized. It should take an integer that specifies how often the function has to be run. Make sure you divide the resulting run time by this number.
3. Use functools.wraps to preserve the function attributes including the docstring that you wrote.
4. Make the time measurement optional by using a global switch in the module that can be set to True or
False to turn time measurement on or off.
5. Write another decorator that can be used with a class and registers every class that it decorates in a dictionary.
'''
