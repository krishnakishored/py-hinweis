class A:
    
    def __init__(self):
        print("An instance of A is initialized")
    
    #The __call__ method is called, if the instance is called "like a function", i.e. using brackets.
    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)


class Fibonacci:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]


def decorator1(f):
    def helper():
        print("Decorating", f.__name__)
        f()
    return helper

@decorator1
def foo():
    print("inside foo()")



class decorator2:
    def __init__(self,f):
        self.f = f

    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()    

@decorator2
def foo2():
    print("inside foo2()")




if __name__=="__main__":
    
    x = A()
    print("now calling the instance")
    x(3,4,x=11,y=10)
    print("Let's call it again:")
    x(3, 4, x=11, y=10)
    fib = Fibonacci()
    for i in range(15):
        print(fib(i),end=" ")
    print("\n")
    foo()
    foo2()
