class A():  
    
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


class Robot:
    '''
    Every private attribute of our class has a getter and a setter
    ''' 
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year
        
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
            
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name    

    def set_build_year(self, by):
        self.__build_year = by
        
    def get_build_year(self):
        return self.__build_year    
    
    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)

# Destructor
# If a base class has a __del__() method, the derived class's __del__() method, if any, must explicitly call it to ensure proper deletion of the base class part of the instance. 

class Robot2():
    
    def __init__(self, name):
        print(name + " has been created!")
        
    def __del__(self):
        print ("Robot has been destroyed")
        # print (self.name + " says bye-bye!") # We are accessing an attribute which doesn't exist anymore.





if __name__ == "__main__":
    x = A()
    print(x.pub)        
    print(x._prot)        
    # print(x.__priv) # AttributeError: 'A' object has no attribute '__priv'
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")

    x = Robot2("Tik-Tok")
    y = Robot2("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y





    # There is a way to access a private attribute directly. 
    # In our example, we can do it like this: x._Robot__build_year 
    # You shouldn't do this under any circumstances! 