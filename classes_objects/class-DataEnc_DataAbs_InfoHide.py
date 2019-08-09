class Robot:
 
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot(\"" + self.name + "\"," +  str(self.build_year) +  ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " +  str(self.build_year)

        
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")
            
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name    

    def set_build_year(self, by):
        self.build_year = by
        
    def get_build_year(self):
        return self.build_year    


if __name__ == "__main__":

    import datetime
    today = datetime.datetime.now()
    print(str(today))
    print(repr(today)) # official representation of the datetime object.
    today2 = eval(repr(today)) # Using this string representation, we can reconstruct the obj
    print(str(today2)) # The eval() built-in function accepts a string and converts it to a datetime object.

    # We can see that eval(repr_s) returns again a datetime.datetime object. 
    # The String created by str can't be turned into a datetime.datetime object by parsing it. 

    x = Robot("Marvin", 1979)
        
    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))
    
    # new = eval(x_str) # error
    x_repr = repr(x)
    new = eval(x_repr)
    print(new)
    print("Type of new:", type(new))
    print("Type of x:", type(x))



# x = Robot("Henry", 2008)
# y = Robot()
# y.set_name("Marvin")
# x.say_hi()
# y.say_hi()
    

# x = Robot()
# x.set_name("Henry")
# x.say_hi()
# y = Robot()
# y.set_name("David")
# y.say_hi()
# y.set_name(x.get_name())
# y.say_hi()


'''
Encapsulation is seen as the bundling of data with the methods that operate on that data. 
Information hiding on the other hand is the principle that some internal information or data is "hidden", so that it can't be accidentally changed. 
Data encapsulation via methods doesn't necessarily mean that the data is hidden.  You might be capable of accessing and seeing the data anyway, but using the methods is recommended. 
This means data abstraction is the broader term: Data Abstraction = Data Encapsulation + Data Hiding 

'''
