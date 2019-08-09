# https://www.python-course.eu/python3_multiple_inheritance.php

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
    
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    # pass
    def m(self):
        print("m of D called")


class D2(B,C):
    '''
    the method m of D should execute the code of m of B, C and A as well, when it is called.
    '''
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)
        A.m(self)


class A3:
    def m(self):
        print("m of A3 called")

class B3(A3):
    def m(self):
        print("m of B3 called")
        A3.m(self)
    
class C3(A3):
    def m(self):
        print("m of C3 called")
        A3.m(self)

class D3(B3,C3):
    def m(self):
        print("m of D3 called")
        B3.m(self)
        C3.m(self)


#Pythonic way to solve A3 getting called twice
class A5:
    def m(self):
        print("m of A5 called")

class B5(A5):
    def m(self):
        print("m of B5 called")
        super().m()
    
class C5(A5):
    def m(self):
        print("m of C5 called")
        super().m()

class D5(B5,C5):
    def m(self):
        print("m of D5 called")
        super().m()



# Super function is often used when instances are initialized with __init__ method
class A6:
    def __init__(self):
        print("A6.__init__")

class B6(A6):
    def __init__(self):
        print("B6.__init__")
        super().__init__()
    
class C6(A6):
    def __init__(self):
        print("C6.__init__")
        super().__init__()


class D6(B6,C6):
    def __init__(self):
        print("D6.__init__")
        super().__init__()


if __name__ == "__main__":
    x = D()
    x.m()  # m of D called
    
    # We can also explicitly call the methods m of the other classes via the class name,
    C.m(x)
    B.m(x)
    A.m(x
    )
    print('calling D2')
    x = D2()
    x.m()

    print('calling D3')
    x = D3()
    x.m()# A3 is called twice
    
    print('calling D4 - usage of super()')
    x = D5()
    x.m()# A3 is called twice
    

    # Super Function in __init__
    d6 = D6()
    c6 = C6()
    a6 = A6()
    '''
    The question arises how the super functions makes its decision.
    How does it decide which class has to be used?
    As we have already mentioned, it uses the so-called method resolution order(MRO). 
    It is based on the "C3 superclass linearisation" algorithm. This is called a linearisation, because the tree structure is broken down into a linear order. 
    The mro method can be used to create this list
    '''

    print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]