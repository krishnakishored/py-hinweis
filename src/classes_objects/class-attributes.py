#  https://www.python-course.eu/python3_object_oriented_programming.php
#  https://www.python-course.eu/python3_class_and_instance_attributes.php


class Robot:
    pass

class Robot_Asimov:
    Three_Laws = (
        """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
        """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
        """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
    )

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year


class Robot_Static:
    __counter = 0

    def __init__(self):
        type(self).__counter +=1

    @staticmethod
    def RobotInstances():
        return Robot_Static.__counter


class Robot_ClassMethod:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @classmethod
    def RobotInstances(cls):
        return cls, Robot_ClassMethod.__counter
        

'''
Binding attributes to objects is a general concept in Python. 
Even function names can be attributed. You can bind an attribute to a function name in the same way 
'''
def g(x):
    return 42

'''
This can be used as a replacement for the static function variables of C and C++, 
which are not possible in Python. We use a counter attribute in the following example: 

'''

def f(x):
    f.counter = getattr(f, "counter", 0) + 1 
    return "Monty Python"


class C: 
    '''
    how you can count instance with class attributes.
    '''
    counter = 0

    def __init__(self): 
        type(self).counter += 1 # we could have written C.counter instead of type(self).counter, because type(self) will be evaluated to "C" anyway

    def __del__(self):
        type(self).counter -= 1


class Pets:
    name = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))


    @staticmethod
    def about2():
        print("This class is about {}!".format(Pets.name))   
    
class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"

class Cats(Pets):
    name = "cats"



class fraction(object):
    '''
    We have defined a static gcd function to calculate the greatest common divisor of two numbers. 
    the greatest common divisor (gcd) of two or more integers (at least one of which is not zero), is the largest positive integer that divides the numbers without a remainder. 
    For example, the 'GCD of 8 and 24 is 8. The static method "gcd" is called by our class method "reduce" with "cls.gcd(n1, n2)". "CLS" is a reference to "fraction". 
    '''

    def __init__(self, n, d):
        self.numerator, self.denominator = fraction.reduce(n, d)
        

    @staticmethod
    def gcd(a,b):
        while b != 0:
            a, b = b, a%b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)

    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)


if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2) #True,  y2 is an alias name for y
    print(y == x)  #False

    # We can dynamically create arbitrary new attributes for existing instances of a class. 
    # We do this by joining an arbitrary name to the instance name, separated by a dot "."

    x.name= "Marvin"
    x.build_year = "1979"
    print(x.name)

    y.build_year = "1993"
    print(y.build_year)
    print(x.__dict__) # {'name': 'Marvin', 'build_year': '1979'}
    print(y.__dict__)
    print(y2.__dict__)
    Robot.brand = "Thales"
    x.brand="HTS"
    print(Robot.__dict__)
    # {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Robot' objects>, '__weakref__': <attribute '__weakref__' of 'Robot' objects>, '__doc__': None, 'brand': 'Thales'}
    print(y.brand) # Thales

    # If you try to access y.brand, Python checks first, if "brand" is a key of the y.__dict__ dictionary. 
    # If it is not, Python checks, if "brand" is a key of the Robot.__dict__. 
    # If so, the value can be retrieved. Else an attribute error is raised

    print(x.brand) # HTS

    # By using the function getattr, you can prevent this exception, if you provide a default value as the third argument:
    print(getattr(x,'energy',"not an attribute"))
    x.energy="high"
    print(getattr(x,'energy',"not an attribute")) # high
    
    g.x=43
    print(g(1))  # 42
    print(g.x) # 43

    for i in range(10):
        f(i)
    print(f.counter) # 10
    f(0)
    f(100)
    print(f.counter) # 12 - the no.of times the function is called

    print(x.__dict__) # {'name': 'Marvin', 'build_year': '1979', 'brand': 'HTS', 'energy': 'high'}
    print(x.__class__.__dict__) # {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Robot' objects>, '__weakref__': <attribute '__weakref__' of 'Robot' objects>, '__doc__': None, 'brand': 'Thales'}
    print(Robot.__dict__) # {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Robot' objects>, '__weakref__': <attribute '__weakref__' of 'Robot' objects>, '__doc__': None, 'brand': 'Thales'}


    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))


    for num,text in enumerate(Robot_Asimov.Three_Laws):
        print(str(num+1) + ":" + text) # we can access a class attribute via instance or via the class name


    print(Robot_Static.RobotInstances())
    x = Robot_Static()
    print(x.RobotInstances())
    y = Robot_Static()
    print(x.RobotInstances())
    print(Robot_Static.RobotInstances())


    print(Robot_ClassMethod.RobotInstances())
    x = Robot_ClassMethod()
    print(x.RobotInstances())
    y = Robot_ClassMethod()
    print(x.RobotInstances())
    print(Robot_ClassMethod.RobotInstances())


    p = Pets()
    p.about()  # This class is about pet animals!
    d = Dogs() 
    d.about() # This class is about 'man's best friends' (Frederick II)!
    c = Cats() # This class is about cats!
    c.about()


    p.about2() # This class is about pet animals!
    d.about2() # This class is about pet animals!
    c.about2() # This class is about pet animals!


    f = fraction(30,60)
    print(f) # 1/2