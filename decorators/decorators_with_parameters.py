#Decorators with Parameters

def evening_greeting(func):
    def function_wrapper(*args,**kwargs):
        print("Good evening, "+func.__name__)
        func(*args,**kwargs)
    return function_wrapper        


def morning_greeting(func):
    def function_wrapper(x):
        print("Good morning, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

#decorators with parameters
def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr+", "+func.__name__+" returns")
            func(x)
        return function_wrapper
    return greeting_decorator



@evening_greeting
def foo(x):
    print(42)    

def foo2(x):
    print(143)    


@greeting("καλημερα")
def bar(x):
    print(56)    

if __name__=="__main__":
    foo("Hi")
    bar("Hello")
    
    # greeting2 = greeting("καλημερα")
    # foo2 = greeting2(foo2)
    # foo2("Hi") 

    foo2 = greeting("καλημερα")(foo2)
    foo2("Halo")


