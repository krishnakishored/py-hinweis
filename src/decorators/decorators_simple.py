def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))


@our_decorator
def bar(x):
    return print("Hi I am a bar")

@our_decorator
def succ(n):
    return n + 1

from math import sin, cos
from random import random, randint, choice


def our_decorator_generalized(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

if __name__=="__main__":
    print("We call foo before decoration:")
    foo("Hi")

    print("We now decorate foo with f:")
    foo = our_decorator(foo) #foo becomes a reference to the 'function_wrapper'.

    print("We call foo after decoration:")
    foo(42)

    bar(786)

    succ(10)

    sin = our_decorator(sin)
    cos = our_decorator(cos)
    
    for f in [sin,cos]:
        f(3.1415)

    random = our_decorator_generalized(random)
    randint = our_decorator_generalized(randint)
    choice = our_decorator_generalized(choice)

    random()
    randint(3, 8)
    choice([4, 5, 6])



# class A:
#     def __init__(self,xyz=0):
#         self.xyz = 0
#         print("An instance of A was initialized")

#     def getxyz(self):
#         print("xyz = "+ str(self.xyz))

# #a = A();
# #print(str(a.getxyz()))

# def my_decorator(func):
#     def function_wrapper(*args,**kwargs):
#         print("before calling func: "+ func.__name__)
#         func(*args, *kwargs)
#         print("after calling func: "+ func.__name__)
#     return function_wrapper

# @my_decorator
# def SimpleHi(x):
#     print("Hello Mr."+str(x))

# #SimpleHi("Apple")






# class decorator2:
#     def __init__(self, f):
#         self.f = f
#     def __call__(self,*args,**kwargs):
#         print("Decorating", self.f.__name__)
#         self.f(*args,**kwargs)


# class inko_class:
#     def _init__(self,a,b):
#         self.a = a
#         self.b = b
#     def inko_method(self):
#         print(str(self.a+self.b))
#     def __call__(self,a,b):
#         self.inko_method(self)

# a = inko_class(1,3)

# @decorator2
# def foo(x):
#     print("inside foo() " + str(x))

# #foo("Hello")

