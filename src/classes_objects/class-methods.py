'''
The proper way to define a method:
 - Instead of defining a function outside of a class definition and binding it to a class attribute, we define a method directly inside (indented) of a class definition.
 - A method is "just" a function which is defined inside of a class.
 - The first parameter is used a reference to the calling instance.
 - This parameter is usually called self.
'''


class Robot:
    def __init__(self,name=None):
        # print("__init__ has been executed")
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name   

    def set_build_year(self, by):
        self.build_year = by
        
    def get_build_year(self):
        return self.build_year    
     

def hi(obj):
    print("Hi I'm " + obj.name)

# It's possible to define a method like this, But Do Not Do it!
class Robot2:
    say_hi = hi



class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)
    
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)




if __name__=="__main__":
    a = Robot2()
    a.name = "Marvin"
    a.say_hi() # Hi I'm Marvin

    # Robot.say_hi(x)". and "x.say_hi()" are equivalent. 

    x = Robot()
    # x.say_hi()
    # y= Robot("Marvin")
    # y.say_hi()
    x.set_name("Henry")
    x.say_hi()
    y = Robot("Lewis") # uses __init__
    # y.set_name(x.get_name())
    print(y.get_name())








'''
For a Class C, an instance x of C and a method m of C the following three method calls are equivalent:
type(x).m(x, ...)
C.m(x, ...)
x.m(...)

'''




















'''
We have seen that a method differs from a function only in two aspects:
It belongs to a class, and it is defined within a class
The first parameter in the definition of a method has to be a reference to the instance, which called the method. 
This parameter is usually called "self".


For a Class C, an instance x of C and a method m of C the following three method calls are equivalent:
type(x).m(x, ...)
C.m(x, ...)
x.m(...)


Data Abstraction = Data Encapsulation + Data Hiding 


'''

