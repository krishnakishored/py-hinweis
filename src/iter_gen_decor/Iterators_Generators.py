'''
Iterators are objects that have a next and __iter__ methods:
__iter__  has  to  return  the  iterator  itself  and  next  should  return  the  next  element  and  raise
StopIteration when finished.
'''
class CountDown(object):
    def __init__(self, start):
         self.counter = start + 1
    #  def next(self): # __next__ in Python 3
    def __next__(self): # __next__ in Python 3
         self.counter -= 1
         if self.counter <= 0:
             raise StopIteration
         return self.counter
    def __iter__(self):
         return self

cd = CountDown(3)
print("iterators: objects with __iter__ & __next__:")
for i in cd:
    print(i,end=" ")

#A sequence can be turned into an iterator using the built-in function iter:
print("\nusing built-in iter:")
i = iter(range(5,0,-1))
print(next(i),end=" ")
print(next(i),end=" ")
print(next(i),end=" ")
print(next(i),end=" ")
print(next(i))
#print(next(i)) #StopIteration


'''
Generator Functions : We can generate iterators with the help of generators.
A generator function is a function with the keyword yield in its body:
'''

def count_down(value):
    for i in range(value,0,-1):
        yield i


i2 = count_down(2)
print(next(i2),end=" ")
print(next(i2))
#print(next(i2)) #StopIteration

'''
Generator Expressions:  look just like list comprehensions but don't use square brackets:
'''
print("Generator Expressions:")
exp = (x for x in range(5, 0, -1)) # with [] : print(next()) - TypeError: 'list' object is not an iterator
for x in exp:
    print(x, end=" ")

print("\nyield as coroutine:")
#The yield statement also excepts values that can be sent to the generator. Therefore, we call it a coroutine:
def show_upper():
    while True:
        text = yield
        print(text.upper())
s = show_upper()

#s.send('Hello')#TypeError: can't send non-None value to a just-started generator
next(s) # We need to call next at least once in order to get to yield where we can send something into the coroutine
s.send('Polo')
s.send('Bolo')
s.send('Solo')


#Since this is common thing to do, we can use a decorator that takes care of the first call to next:
def init_coroutine(func):
    def init(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return init

@init_coroutine
def show_lower():
    while True:
        text = yield
        # print(text.lower())
        print(text)


l = show_lower()
#next(l) # Not required
print("using init_coroutine decorator")
l.send('Polo')
l.send('Bolo')
l.send('Solo')

#Sending and yielding at the same time
@init_coroutine
def show_upper_2():
    result = None
    try:
        while True:
            text = yield result
            result = text.upper()
    except  GeneratorExit: #Even if we catch this exception inside the coroutine, it will be closed:
        print('done generating!')

'''

s2 = show_upper_2()
print("both sender and receiver:")
res = s2.send('lolo')
print(res)
s2.close() #Calling close will throw a GeneratorExit exception inside the coroutine:
res = s2.send('golo') #StopIteration

'''
#Analogous to files that are closed when the get out of scope, a GeneratorExit is raised when the object is garbage collected:
s3 = show_upper_2()
del s3 # done generating!
