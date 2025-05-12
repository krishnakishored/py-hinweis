
#local functions

# LEGB - checking starts with the local scope, then the enclosing, then global and finally the built-in scope

def my_function():
    #The function my_local_function is a local function as it is only available inside my_function and can only be used within the function.
  def my_local_function():
    print('I am a local function, local to my_function')
  print('I am not a local function') 
  my_local_function()


def remove_first_item(my_array):
  def get_first_item(s):
    return s[0]
  my_array.remove(get_first_item(my_array))
  return my_array
    

def enclosing_func():
  def local_func():
    print ('I am a local function')
  return local_func()
 
 

# Closure
def outer_function():
    x = 5
    #The local function is able to reference the outer scope through closures. 
    # Closures maintain references to objects from the earlier scope.
    def inner_fun(y=3):
        return x+y
    return inner_fun


def multiply_by(num):
  def multiply_by_num(k):
    return num * k
  return multiply_by_num

def startAt(start):
    def incrementBy(inc):
        return start + inc
    return incrementBy

def startAt_lambda(start):
    return lambda inc:start+inc


if __name__=="__main__":
    my_function()
    print(remove_first_item(['1','2','3'])) #['2', '3']
    # print(get_first_item([1,2,3,4])) #NameError: name 'get_first_item' is not defined
    enclosing_func() #I am a local function

    a = outer_function()
    print(a()) #8

    fives = multiply_by(5)
    print(fives(10)) #50

    closure1 = startAt(10)
    closure2 = startAt(100)

    print(closure1(4)) # 4
    print(closure2(345)) #445

    f = startAt(10)
    g = startAt(100)

    print('type(f)=%s' %(type(f))) 
    print('f.__closure__=%s' %(f.__closure__)) 
    print('type(f.__closure__[0])=%s' %(type(f.__closure__[0]))) 
    print('f.__closure__[0].cell_contents=%s' %(f.__closure__[0].cell_contents)) 

    print('type(g)=%s' %(type(g))) 
    print('g.__closure__=%s' %(g.__closure__)) 
    print('type(g.__closure__[0])=%s' %(type(g.__closure__[0]))) 
    print('g.__closure__[0].cell_contents=%s' %(g.__closure__[0].cell_contents)) 

    a = startAt_lambda(50)
    b = startAt_lambda(75)

    print(a(1), b(2)) # 51 77
    
'''
https://www.codementor.io/moyosore/a-dive-into-python-closures-and-decorators-part-1-9mpr98pgr
https://www.bogotobogo.com/python/python_closure.php
'''