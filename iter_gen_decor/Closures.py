#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory
'''
Firstly, a Nested Function is a function defined inside another function. It's very important to note that the nested functions can access the variables of the enclosing scope. However, at least in python, they are only readonly. However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.
'''

def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    data_transmitter()

transmit_to_space("Test message")

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        #nonlocal number
        number=3 #Without the nonlocal keyword, the output would be "3 9"
        print("in printer:",number)
    printer()
    print("within print_msg: ",number)

print_msg(9)

'''
Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures. That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.
'''

def multiplication_with_n(number):
    def multiply(n):
        return number*n
    return multiply

mul_with_3 = multiplication_with_n(3)
print(mul_with_3(10))
