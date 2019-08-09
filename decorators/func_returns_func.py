#Two different kinds of decorators in Python: Function decorators, Class decorators

def succ(x):
    return x+1

def f():
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")

    print("This function is 'f'")
    print("I am calling 'g' now")
    g()
                 

def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!" 
    return result

## Functions as parameters
def g1():
    print("Hi, it's me 'g1'")
    print("Thanks for calling me")

def f1(func):
    print("Hi, it's me 'f1'")
    print("I will call 'func' now")
    func()
    print("func's real name is " + func.__name__) 


import math
def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res

## Functions returning functions : 
# The output of a function is also a reference to an object. Therefore functions can return references to function objects.

def f2(x):
    def g2(y):
        return y + x + 3 
    return g2

## Polynomial Factory

if __name__=="__main__":
    successor = succ
    print(successor(32))
    del succ # we can delete either "succ" or "successor" without deleting the function itself
    print(successor(100))
    # f()
    print(temperature(20))
    f1(g1)

    print(foo(math.sin))
    print(foo(math.cos))

    nf1 = f2(1)
    nf2 = f2(20)

    print(nf1(1))
    print(nf2(1))


# https://www.python-course.eu/python3_decorators.php