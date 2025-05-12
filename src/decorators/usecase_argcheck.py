#argument checking
def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper
    

# @argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)



## Counting Function Calls with Decorators

def call_counter(func):
    def wrapper(*args,**kwargs):
        wrapper.calls +=1
        return func(*args,**kwargs)
    wrapper.calls=0
    return wrapper

@call_counter
def succ(x):
    return x + 1

@call_counter
def mul1(x, y=1):
    return x*y + 1


#1. We check if the positional arguments to a function call are of a certain type.
import functools

def check(*argtypes):
    """Function argument type checker."""
    def _check(func):
        """Takes the function."""
        @functools.wraps(func)
        def __check(*args):
            """Takes the arguments"""
            if len(args) != len(argtypes):
                msg = 'Expected %d but got %d arguments' % (len(argtypes), len(args))
                raise TypeError(msg)
            for arg, argtype in zip(args, argtypes):
                if not isinstance(arg, argtype):
                    msg = 'Expected %s but got %s' % (argtypes, tuple(type(arg) for arg in args))
                    raise TypeError(msg)
            return func(*args)
        return __check
    return _check

if __name__=="__main__":
    
    for i in range(1,10):
	    print(i, factorial(i))
    factorial = argument_test_natural_number(factorial)
    # print(factorial(-1))


    print(succ.calls) #0
    for i in range(10):
        succ(i)
    
    print(succ.calls) #10

    mul1(3, 4)
    mul1(4)
    mul1(y=3, x=2)
    
    print(mul1.calls) # 3