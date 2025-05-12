'''
Decorator provide a very useful method to add functionality to existing functions and classes. 
Decorators are functions that wrap other functions or classes.
One example for the use of decorator are static methods. Static methods could be function in the global scope
but are defined inside a class. There is no``self`` and no reference to the instance.
'''
#Before Python 2.4 they had to defined like this:
class C(object):
    def func():
        "No self here"
        print('Method used as function')
    func = staticmethod(func)

    @staticmethod
    def func_2():
        print('func_2: Method used as function')
'''Because the staticmethod call is after the actual definition of the method, it can be difficult to read an easy
to be overlooked. Therefore, the new @ syntax is used before the method definition but does the same:'''

#The same works for class methods that take a class objects as argument instead of the instance (aka self).
c1 = C()
c1.func()
c1.func_2()
#----------------------------------------------------------------------------------

#writing our own decorator
'''
def hello1(func):
    print('Hello',func.__name__)

@hello1
def add(a,b):
    return a+b

add(1,23)# 'Hello add' gets printed but TypeError: 'NoneType' object is not callable

So,  even  it  is  not  enforced  by  the  interpreter,  decorators  usually  make  sense if  they  behave  in  a  certain  way.
It  is  strongly  recommended  that  a  function  decorator always  returns  a  function  object  and  a  class  decorator  always  returns  a  class  object.  A  function  decorator should  typically  either  return  a  function  that  returns  the  result  of  the  call  to  the  original  function  and  do something in addition or return the original function itself.
'''
def hello(func):
    """decorator function"""
    def call_func(*args,**kwargs):
        """Takes a arbitrary number of positional and keyword arguments."""
        print('Hello')
        # Call original function and return its result.
        return func(*args,**kwargs)
    # Return function defined in this scope.
    return call_func

@hello
def add(a,b):
    return a+b

sum = add(11,23)
print(sum)

#parameterized decorators
'''
Decorators can take arguments. We redefine our decorator.
The outermost function takes the arguments,
    the next more inner function takes the function and
        the innermost function will be returned and will replace the original function:
'''
def say(text):
    def _say(func):
        def call_func(*args,**kwargs):
            print(text)
            return func(*args,**kwargs)
        return call_func
    return _say

#@say('Namasthe')
@say('Sawadee Krap')
def add(a,b):
    return a+b

sum = add(100,20)
print(sum)

# Chaining Decorators : We can use more than one decorator for one function:
@say('How do you do?')
@say('Guten Morgen!')
@hello
def add(a,b):
    return a+b

sum = add(5,6)
print(sum)

#class decorator - Since Python 2.6 we can use decorators for classes too:
def mark(cls):
    cls.added_attr = 'I am decorated.'
    return cls
#It  is  important  to  always  return  a  class  object  from  the  decorating  function.  Otherwise  users  cannot  make instances from our class.

@mark
class A(object):
    pass
print(A.added_attr, A.__name__)

#Best practices
import functools
#We  could  manually  set  the  docstring  of  our  wrapped  function  to  remain  the  same.  But  the  module functools in the standard library helps us here:
def hello_wrap(func):
    @functools.wraps(func) # without this add.__doc__ prints 'Wrapper'
    def call_func(*args, **kwargs):
        """Wrapper."""
        print('Hello')
        return func(*args, **kwargs)
    return call_func

@hello_wrap
def add(a,b):
    """Add two objects."""
    return a+b

print(add.__doc__) #Add two objects.

#calling recursive functions
print('calling recursive functions:')
@hello_wrap
def recursive(x):
    if x:
        x -=1
        print(x)
        recursive(x)
'''
When we decorate a recursive function the wrapper will also be called recursively:
In most cases this is not desirable. Therefore, recursive function should not be decorated.
Don't assume you have only one decorator
'''
recursive(3)
