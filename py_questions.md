```Python general questions```
------------------------------
1) what is the difference between python and other laungages ??
2) Mention few benefits of using Python?
3) Does Python allow arguments Pass by Value or Pass by Reference?
4) Why is the “pass” keyword used for in Python?
5) Why is <__init__.py> module used for?
6) Differentiate between .py and .pyc files?
7) Explain how Python does Compile-time and Run-time code checking?
8) How memory is managed in Python?
9) what is the use of setup.py in python
10) what is the use of __init__==__main__: condition in python??
11) what is the type of *args and **kargs ??
12) difference between %s and %r in python
13) What is module and package in Python?
14) How will you set a global variable inside a function?
15) How will you share global variables across modules?
16) What are the tools that help to find bugs or perform static analysis?
17) As Everything in Python is an Object, Explain the characteristics of Python's Objects.
18) Diff between __repr__ and ___str___ methods
      If you apply str or repr to an object, Python is looking for a corresponding method __str__ or __repr__ in the class definition of the object. If the method does exist, it will be called. 
    
    __str__ is always the right choice, if the output should be for the end user or in other words, if it should be nicely printed. 
    __repr__ on the other hand is used for the internal representation of an object. The output of __repr__ should be - if feasible - a string which can be parsed by the python interpreter. The result of this parsing is in an equal object. 
    This means that the following should be true for an object "o": 
      o == eval(repr(o)) 




19) Are there equivalents to pointers & references in C/C++
20) How do create an executable with .py files
21) use of __name__=="__main__"

      Every module in python has a special attribute called __name__ . 
      The value of __name__  attribute is set to '__main__'  when module run as main program. 
      Otherwise the value of __name__  is set to contain the name of the module.

22) @property
23) recursive functions 
24) Memoization 
      * https://www.python-course.eu/python3_memoization.php
      > Memoisation is a technique used in computing to speed up programs. This is accomplished by memorizing the calculation results of processed input such as the results of function calls.French Jesuit Claude-Gaspar Bachet phrased it.

25) logging module
      * https://pymotw.com/3/logging/index.html#module-logging

Python string questions:-
--------------------------
1) What is slicing in Python? Explain with example.
2) What is a negative index in Python?
3) What is the best way to split a string in Python?
4) What is the right way to transform a Python string into a list?
5) How will you convert a string to a number in Python?


Python library functions
--------------------------

python iterators related questions:-
-------------------------------------
1) What are iterators in Python?
2) What are generators in Python? and yield keyword use in python ??
      https://python-course.eu/python3_generators.php

      > An iterator can be seen as a pointer to a container, e.g. a list structure that can iterate over all the elements of this container. The iterator is an abstraction, which enables the programmer to access all the elements of a container (a set, a list and so on) without any deeper knowledge of the data structure of this container object.

      > Generators are a special kind of function, which enable us to implement or generate iterators. Iterators are a fundamental concept of Python. 
      
      > On the surface generators in Python look like functions, but there is both a syntactic and a semantic difference. 
      One distinguishing characteristic is the yield statements. The yield statement turns a functions into a generator. 
      
      A generator is a function which returns a generator object. This generator object can be seen like a function which produces a sequence of results instead of a single object. This sequence of values is produced by iterating over it, e.g. with a for loop. 
      
      The values, on which can be iterated, are created by using the yield statement. The value created by the yield statement is the value following the yield keyword. The execution of the code stops when a yield statement has been reached. The value behind the yield will be returned. The execution of the generator is interrupted now. As soon as "next" is called again on the generator object, the generator function will resume execution right after the yield statement in the code, where the last call exited. The execution will continue in the state in which the generator was left after the last yield. This means that all the local variables still exists, because they are automatically saved between calls. 
      
      This is a fundamental difference to functions: functions always start their execution at the beginning of the function body, regardless where they had left in previous calls. They don't have any static or persistent values. There may be more than one yield statement in the code of a generator or the yield statement might be inside the body of a loop. If there is a return statement in the code of a generator, the execution will stop with a StopIteration exception error if this code is executed by the Python interpreter. 
      The word "generator" is sometimes ambiguously used to mean both the generator function itself and the objects which are generated by a generator. 



      Everything which can be done with a generator can also be implemented with a class based iterator as well. 
      But the crucial advantage of generators consists in automatically creating the methods __iter__() and next(). 
      Generators provide a very neat way of producing data which is huge or infinite. 



3) list comprehensions in python ??
   * https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3
   > List comprehension is an elegant way to define and create list in Python
     list_variable = [x for x in iterable]
    
4) zip function in python ??
5) What is the use of enumerate() in Python?
6) lamda expressions in python ???
7) Map,reduce and filter functions in python ???

      s> The map() built-in function is another “iterator operator” that, in its simplest form, applies a single-parameter function to each element of an iterable one element at a time:


8) What is the difference between Xrange and range?
9) Difference between iterable and iterator
     https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration
     https://python-course.eu/python3_iterable_iterator.php

    > In Python, iterable and iterator have specific meanings.
    An iterable is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__ method that can take sequential indexes starting from zero (and raises an IndexError when the indexes are no longer valid). So an iterable is an object that you can get an iterator from.
    - Iterables can return their elements one at time.
    - Technically, any Python object that implements the .__iter__() or .__getitem__() methods is iterable.
    - The iter() built-in function, when called on an iterable, returns an iterator object for that iterable:

    > An iterator is an object with a next (Python 2) or __next__ (Python 3) method.
    Whenever you use a for loop, or map, or a list comprehension, etc. in Python, the next method is called automatically to get each item from the iterator, thus going through the process of iteration.
    
    > The Python itertools module is a collection of tools for handling iterators. Simply put, iterators are data types that can be used in a for loop. The most common iterator in Python is the list


    > Iterators are themselves also iterable, with the distinction that their __iter__() method returns the same object (self), regardless of whether or not its items have been consumed by previous calls to next().

    Quiz: Do you see how...
    - every iterator is an iterable?
    - a container object's __iter__() method can be implemented as a generator?
    - an iterable plus a __next__ method is not necessarily an iterator?
    
10) Set comprehension
      > A set comprehension is similar to a list comprehension, but returns a set and not a list. Syntactically, we use curly brackets instead of square brackets to create a set.

11) what are itertools?
      > https://realpython.com/python-itertools/

Python mechanism related questions:-
------------------------------------
1) Explain the use of with statement?  (python context manager mechanism)
      > Locks implement the context manager API and are compatible with the with statement. Using with removes the need to explicitly acquire and release the lock.

      
2) Whenever Python exists Why does all the memory is not de-allocated / freed
   (python garbage collector mechanism when Python exits?)
3) Explain about Python decorators?

      > A decorator in Python is any callable Python object that is used to modify a function or a class. Decorator is simply a callable object that takes a function as an input parameter
      > Decorators can take arguments. We redefine our decorator.The outermost function takes the arguments,the next more inner function takes the function and the innermost function will be returned and will replace the original function
      > We can pass arguments to decorators
      > Using wraps from functools we can avoid losing the attributes of the original function 
            __name__ (name of the function),
            __doc__ (the docstring) and
            __module__ (The module in which the function is defined)

      > The __call__ method of a class is called, if the instance is called "like a function", i.e. using brackets.

      > Use cases - argument checking, counting the no.of function calls

            
4) What is Pickling and how does it different from Unpickling?
5) Decorators used for Polynomial functions in Python
      * https://www.python-course.eu/polynomial_class_in_python.php
6) Callable objects of Python
      > A callable object is an object which can be used and behaves like a function but might not be a function. It is possible to define classes in a way that the instances will be callable objects. The __call__ method is called, if the instance is called "like a function", 
7)  write a fibonacci class using __call__
8) Closures 
      > The local function is able to reference the outer scope through closures. Closures maintain references to objects from the earlier scope.   
      Closure is commonly used in what is referred to as Function Factory - these are functions that return other functions. 
      a closure is a combination of code and scope.  a closure is a function (object) that remembers its creation environment (enclosing scope).
      A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory
9) Global & non-local
      > global is a python keyword that introduces names from global namespace into the local namespace.
      The nonlocal keyword allows us to introduce names from enclosing namespace into the local namespace. 

File realted questions:-
-------------------------
1) How do you check the file existence and their types in Python?
2) How do you open a file in python?? and why??
3) How do you check list of files in the given path in python ??
4) How do you check whether file is exist or not in python
5) How do you perform copy file cmd in python ??
6) Explain how to delete a file in Python?


Collections(list,tuple,set,dictionary):-
-----------------------------------------
1) When to use list ?? tuple ?? set ?? and dictionary in python ??
2) List out the each collections(list,tuple,set and dictinary)object type. i.e
   List which are mutable objects and which are immutable objects ??
   * https://www.programiz.com/python-programming/list

3) How will you remove the duplicate elements from the given list?
4) What is the best approach to store a list of an employee’s first and last names?
5) Why don't we use list as dictionary key??


```OOPS```
--------------
1) Is Python object oriented? what is object oriented programming?
2) java type constructor in python??
3) self keyword use in python??
4) Explain Inheritance in Python with an example.
5) Explain polymorphism in python with an static binding and dynamic binding examples ??
6) Method overriding???
7) How instance variables are different from class variables?
8) Can you write code to check whether the given object belongs to a class or its subclass?
9) Abstract class implementation in python ?? can we create object for abstract class ?? if not then how we can call the abstract class members??
10) Super keyword use in python oops concept??
11) Could you please explain MRO(Method resolution order) in python ??
12) Compostion vs inheritance vs aggregation ??
13) Static variables and static methods in python ??
14) Does diamond probelm exist in python ??
15) Does python support multiinheritance ??
16) Does Python supports interfaces like in Java? Discuss.
17) Name and explain the three magic methods of Python that are used in the construction and initialization of custom Objects.
18) What are the different methods Python provides for copying an object?
19) How to prevent class 'a' from being inherited by another class?
    and also how to prevent parent class method 'm' from being inherited by another class?
20) How do you implement constant variables in python ???
21) Exact use of Abstract class??
22) Is there object slicing in Python
23) Magic Methods and Operator Overloading
      * https://www.python-course.eu/python3_magic_methods.php     
24) Attributes vs Properties in a python class
    - properties and attributes are essentially different things in Python.
    - Attributes are created inside of a class. Also we can dynamically create arbitary new attributes for existing classes
    - The instances possess dictionaries __dict__, which they use to store their attributes and their corresponding values: 
    - Python's class attributes and object attributes are stored in separate dictionaries
    - Let's summarize the usage of private and public attributes, getters and setters and properties: 
    Let's assume that we are designing a new class and we pondering about an instance or class attribute "OurAtt". We have to observe the following issues:
      - Will the value of "OurAtt" be needed by the possible users of our class? If not, we can or should make it a private attribute.
      - If it has to be accessed, we make it accessible as a public attribute
      - We will define it as a private attribute with the corresponding property, if and only if we have to do some checks or transformation of the data.
      - Alternatively, you could use a getter and a setter, but using a property is the Pythonic way to deal with it!
            



25) How to add a counter attribute to find the no. of times a function is invoked - Using an attribute of function
26) method vs function: 
A method differs from a function only in two aspects:
      - It belongs to a class, and it is defined within a class
      - The first parameter in the definition of a method has to be a reference to the instance, which called the method. This parameter is usually called "self".
27) __init__ method:
We want to define the attributes of an instance right after its creation. __init__ is a method which is immediately and automatically called after an instance has been created. This name is fixed and it is not possible to chose another name
The __init__ method is used to initialize an instance. 

There is no explicit constructor or destructor method in Python, as they are known in C++ and Java.

28) __del__ method:
There is no "real" destructor, but something similar, i.e. the method __del__. It is called when the instance is about to be destroyed and if there is no other reference to this instance

28) Encapsulation, Data Abstraction, Polymorphism, Inheritance
      Data Abstraction = Data Encapsulation + Data Hiding 

      Encapsulation is often accomplished by providing two kinds of methods for attributes: The methods for retrieving or accessing the values of attributes are called getter methods. Getter methods do not change the values of attributes, they just return the values. The methods used for changing the values of attributes are called setter methods. 

      Python is implicitly polymorphic.We can call a function with various types


----
Exception Handling:-
-----------------------

1) What is an exception?
2) What are Exception Handling? How do you achieve it in Python?
3) Explain different ways to trigger / raise exceptions in your python script ?
4) How many except statements can a try-except block have??
5) When will the else part of try-except-else be executed?
6) When is the finally block executed?
7) Is it necessary that each try block must be followed by a except       block?
8) Can finally block be used without except?
9) Is there any case when finally will not be executed?
10) what happened return statement is in except block
11) will finally run after return??
12) How do you implement custom exception in python ??

----

Concurrency :-
--------------
1) What is the difference between Process and Thread?
> Using threads allows a program to run multiple operations concurrently in the same process space.
2) What are the benefits of multi-threaded programming?
3) What is difference between user Thread and daemon Thread?
4) What are the libraries in Python that support threads?
5) difference between sleep() and wait() method ???
6) join() method use in python ??
7) What is synchronization3 0
8) Explain about Lock ?? and its two states(acquire and release??
9) What is Deadlock? How to analyze and avoid deadlock situation?
10) Explain about wait(),notify() and notifyALL() methods ??
      (Inter process communication methods)
      (Thread condition mechanism)
      * https://pymotw.com/3/threading/#thread-objects
      
11) Why wait(), notify() and notifyAll() methods have to be called from
      synchronized method or block?
12) What is the difference between threading.Lock and threading.RLock?
* To solve your race condition, you need to find a way to allow only one thread at a time into the read-modify-write section of your code. The most common way to do this is called Lock in Python. In some other languages this same idea is called a mutex. Mutex comes from MUTual EXclusion, which is exactly what a Lock does.

* A Lock is an object that acts like a hall pass. Only one thread at a time can have the Lock. Any other thread that wants the Lock must wait until the owner of the Lock gives it up. The basic functions to do this are .acquire() and .release(). A thread will call my_lock.acquire() to get the lock. If the lock is already held, the calling thread will wait until it is released.

* Fortunately, Python’s Lock will also operate as a context manager, so you can use it in a with statement, and it gets released automatically when the with block exits for any reason.

* RLock allows a thread to .acquire() an RLock multiple times before it calls .release(). That thread is still required to call .release() the same number of times it called .acquire(), but it should be doing that anyway.
* Lock and RLock are two of the basic tools used in threaded programming to prevent race conditions.


13) When and how to use Python's RLock??
14) How to terminate a blocking thread?
15) Can we start a thread twice ??
16) Subclassing threads

* The threading library can be used to execute any Python callable in its own thread. To do this, you create a Thread instance and supply the callable that you wish to execute as a target. 
* 
* Threads are executed in their own system-level thread (e.g., a POSIX thread or Windows threads) that is fully managed by the host operating system. Once started, threads run independently until the target function returns.
      - `t.start()`  - When you create a thread instance, it doesn’t start executing until you invoke its start() method (which invokes the target function with the arguments you supplied).   
      `t.is_alive()` - to query a thread instance to see if it's still running       
      `t.join()` - request to join with a thread, which waits for it to terminate          
* Daemonic Threads
      - The interpreter remains running until all threads terminate. For long-running threads or background tasks that run forever, you should consider making the thread daemonic. For example:
      ~~~python
      t = Thread(target=countdown, args=(10,), daemon=True)
      t.start()
      ~~~
      - Daemonic threads can’t be joined. However, they are destroyed automatically when the main thread terminates.
* Due to a global interpreter lock (GIL), Python threads are restricted to an execution model that only allows one thread to execute in the interpreter at any given time. For this reason, Python threads should generally not be used for computationally intensive tasks where you are trying to achieve parallelism on multiple CPUs. They are much better suited for I/O handling and handling concurrent execution in code that performs blocking operations (e.g., waiting for I/O, waiting for results from a database, etc.).

* Event objects are best used for one-time events. That is, you create an event, threads wait for the event to be set, and once set, the Event is discarded. If a thread is going to repeatedly signal an event over and over, you’re probably better off using a Condition object instead. 

*  The threading.Event object allows one thread to signal an event while many other threads can be waiting for that event to happen. The key usage in this code is that the threads that are waiting for the event do not necessarily need to stop what they are doing, they can just check the status of the Event every once in a while.

* A critical feature of Event objects is that they wake all waiting threads. If you are writing a program where you only want to wake up a single waiting thread, it is probably better to use a Semaphore or Condition object instead.

* A Semaphore is a counter with a few special properties. 
- The first one is that the counting is atomic. This means that there is a guarantee that the operating system will not swap out the thread in the middle of incrementing or decrementing the counter. 
- The internal counter is incremented when you call .release() and decremented when you call .acquire().
- The next special property is that if a thread calls .acquire() when the counter is zero, that thread will block until a different thread calls .release() and increments the counter to one.
- Semaphores are frequently used to protect a resource that has a limited capacity. An example would be if you have a pool of connections and want to limit the size of that pool to a specific number

* Timer
- A threading.Timer is a way to schedule a function to be called after a certain amount of time has passed. You create a Timer by passing in a number of seconds to wait and a function to call: `t = threading.Timer(30.0, my_function)`
- You start the Timer by calling .start(). The function will be called on a new thread at some point after the specified time, but be aware that there is no promise that it will be called exactly at the time you want.
- If you want to stop a Timer that you’ve already started, you can cancel it by calling .cancel(). Calling .cancel() after the Timer has triggered does nothing and does not produce an exception.
- A Timer can be used to prompt a user for action after a specific amount of time. If the user does the action before the Timer expires, .cancel() can be called.

* Barrier
- A threading.Barrier can be used to keep a fixed number of threads in sync. When creating a Barrier, the caller must specify how many threads will be synchronizing on it. Each thread calls .wait() on the Barrier. They all will remain blocked until the specified number of threads are waiting, and then the are all released at the same time.
- Remember that threads are scheduled by the operating system so, even though all of the threads are released simultaneously, they will be scheduled to run one at a time.
- One use for a Barrier is to allow a pool of threads to initialize themselves. Having the threads wait on a Barrier after they are initialized will ensure that none of the threads start running before all of the threads are finished with their initialization.


* Perhaps the safest way to send data from one thread to another is to use a Queue from the queue library. To do this, you create a Queue instance that is shared by the threads. Threads then use put() or get() operations to add or remove items from the queue.

* Queue instances already have all of the required locking, so they can be safely shared by as many threads as you wish. When using queues, it can be somewhat tricky to coordinate the shutdown of the producer and consumer. A common solution to this problem is to rely on a special sentinel value, which when placed in the queue, causes consumers to terminate.

* One caution with thread queues is that putting an item in a queue doesn’t make a copy of the item. Thus, communication actually involves passing an object reference between threads. If you are concerned about shared state, it may make sense to only pass im‐ mutable data structures (e.g., integers, strings, or tuples) or to make deep copies of the queued items. 

* A daemon thread will shut down immediately when the program exits. One way to think about these definitions is to consider the daemon thread a thread that runs in the background without worrying about shutting it down.  If a program is running Threads that are not daemons, then the program will wait for those threads to complete before it terminates. Threads that are daemons, however, are just killed wherever they are when the program is exiting.

* ThreadPoolExecutor
      - There’s an easier way to start up a group of threads than the one you saw above. It’s called a ThreadPoolExecutor, and it’s part of the standard library in concurrent.futures 
      

* asynchio
* At the heart of async IO are coroutines. A coroutine is a specialized version of a Python generator function. 



----
Handling JSON
--------------

.... 

Numpy & Pandas
--------------
- Hinton diagram. The size of a square within this diagram corresponds to the size of the value of the depicted matrix. The colour determines, if the value is positive or negative. 

- The main benefits of using numpy arrays should be smaller memory consumption and better runtime behaviour.

- `matplotlib.pyplot`
- `getsizeof` -  for every new element, we need another eight bytes for the reference to the new object. The new integer object itself consumes 28 bytes. 
      The size of a list "lst" without the size of the elements can be calculated with: 64 + 8 * len(lst)

      That an arbitrary integer array of length "n" in numpy needs: 96 + n * 8 Bytes
      whereas a list of integers needs: 64 + 8 * len(lst) + len(lst) * 28


- `time.time()`, `timeit`, `repeat()`
- `dot(a, b, out=None)` - equivalent to matrix multiplication
- There are "real" matrices in Numpy. They are a subset of the two-dimensional arrays. We can turn a two-dimensional array into a matrix by applying the "mat" function. The main difference is if you multiply two two-dimensional arrays or two matrices,  we get real matrix multiplication by multiplying two matrices, but the two-dimensional arrays will be only multiplied component-wise.
-  If we compare two arrays, we don't get a simple True or False as a return value. The comparisons are performed elementswise. This means that we get a Boolean array as a return value.
- `array_equal` returns True if two arrays have the same shape and elements, otherwise False will be returned.
- Broadcasting, which allows to perform arithmetic operations on arrays of different shapes.  Under certain conditions, the smaller array is "broadcasted" in a way that it has the same shape as the larger array.





Bokeh
--------------



Flask
--------------

1. what are microservices
2. data migration
3. Flask & NodeJs - comparision



``` Questions from Cookbook```


interview questions - bogotobogo
--------------------------------

1. List of codes for interview Q & A
2. Merging two sorted list
3. Get word frequency - initializing dictionary
4. Initializing dictionary with list
5. map, filter, and reduce
6. Write a function f() - yield
7. What is __init__.py?
8. Build a string with the numbers from 0 to 100, "0123456789101112..."
9. Basic file processing: Printing contents of a file - "with open"
10. How can we get home directory using '~' in Python?
11. The usage of os.path.dirname() & os.path.basename() - os.path
12. Default Libraries
13. range vs xrange
14. Iterators
15. Generators
16. Manipulating functions as first-class objects
17. docstrings vs comments
18. using lambdda
19. classmethod vs staticmethod 

      * omitting the parameter "self" is class method, it's possible to access the method via the class name, but we can't call it via an instace 
            - We want a method, which we can call via the class name or via the instance name without the necessity of passing a reference to an instance to it. The solution consists in static methods, which don't need a reference to an instance. It's easy to turn a method into a static method. 
            - All we have to do is to add a line with "@staticmethod" directly in front of the method header. It's the decorator syntax. 

      * Static methods shouldn't be confused with class methods. Like static methods class methods are not bound to instances, but unlike static methods class methods are bound to a class. The first parameter of a class method is a reference to a class, i.e. a class object. They can be called via an instance or the class name. 
            - They are often used, where we have static methods, which have to call other static methods. To do this, we would have to hard code the class name, if we had to use static methods. This is a problem, if we are in a use case, where we have inherited classes.
            - They are used in the definition of factory methods


20. Making a list with unique element from a list with duplicate elements
21. *args and **kwargs
22. mutable vs immutable
23. Difference between remove, del and pop on lists
24. Join with new line
25. Hamming distance
26. Floor operation on integers
27. Fetching every other item in the list
28. Python type() - function
29. Dictionary Comprehension
30. Sum
31. Truncating division
32. Differences Python 2 vs Python 3
33. len(set)
34. Print a list of file in a directory
35. Count occurrence of a character in a Python string
36. Make a prime number list from (1,100)
37. Reversing a string - Recursive
38. Reversing a string - Iterative
39. Output?
40. Merging overlapped range
41. Conditional expressions (ternary operator)
42. Function args
43. Unpacking args
44. Finding the 1st revision with a bug
45. Which one has higher precedence in Python? - NOT, AND , OR
46. Decorator(@) - with dollar sign($)
47. Multi-line coding
48. Recursive binary search
49. Iterative binary search
50. Pass by reference
51. Simple calculator
52. iterator class that returns network interfaces
53. Converting domain to ip
54. How to count the number of instances
55. Python profilers - cProfile
56. Calling a base class method from a child class that overrides it
57. How do we find the current module name?
58. Why did changing list 'newL' also change list 'L'?
59. Construction dictionary - {key:[]}
60. Colon separated sequence
61. Converting binary to integer
62. 9+99+999+9999+...
63. Calculating balance
64. Regular expression - findall
65. Chickens and pigs
66. Highest possible product
67. Copy an object
68. Products
69. Pickle
70. Overlapped Rectangles
71. \__dict__
72. Fibonacci I - iterative, recursive, and via generator
73. Fibonacci II - which method?
74. Stack with returning Max item at const time
75. Finding duplicate integers from a list - 1
76. Finding duplicate integers from a list - 2
77. Finding duplicate integers from a list - 3
78. Reversing words 1
79. Parenthesis, a lot of them
80. Palindrome / Permutations
81. Constructing new string after removing white spaces
82. Removing duplicate list items
83. Dictionary exercise
84. printing numbers in Z-shape
85. Factorial
86. lambda, lambda with map/filter/reduce
87. Number of integer pairs whose difference is K
88. Recursive printing files in a given directory
89. Bubble sort
90. What is GIL (Global Interpreter Lock)?
91. Word count using collections
92. Pig Latin
93. List of anagrams from a list of words
94. Write a code sending an email using gmail
95. histogram 1 : the frequency of characters
96. histogram 2 : the frequency of ip-address
97. Creating a dictionary using tuples
98. Getting the index from a list
99. Looping through two lists side by side
100. Dictionary sort with two keys : primary / secondary keys
101. Writing a file downloaded from the web
102. Sorting csv data
103. Reading json file
104. Sorting class objects
105. Parsing Brackets
106. Printing full path
107. str() vs repr()
108. Missing integer from a sequence
109. Polymorphism
110. Product of every integer except the integer at that index
111. What are accessors, mutators, and @property?
112. N-th to last element in a linked list
113. Implementing linked list
114. Removing duplicate element from a list
115. List comprehension
116. .py vs .pyc
117. Binary Tree
118. Print 'c' N-times without a loop
119. Quicksort
120. Dictionary of list
121. Creating r x c matrix
122. str.isalpha() & str.isdigit()
123. Regular expression
124. What is Hashable? Immutable?
125. Convert a list to a string
126. Convert a list to a dictionary
127. List - append vs extend vs concatenate
128. Use sorted(list) to keep the original liste
129. list.count()
130. zip(list,list) - weighted average with two lists
131. Intersection of two lists
132. Dictionary sort by value
133. Counting the number of characters of a file as One-Liner
134. Find Armstrong numbers from 100-999
135. Find GCF (Greatest common divisor)
136. Find LCM (Least common multiple)
137. Draws 5 cards from a shuffled deck
138. Dictionary order by value or by key
139. Regular expression - password check
140. Prime factors : n = products of prime numbers
141. Valid IPv4 address
142. Sum of strings
143. List rotation - left/right
144. shallow/deep copy
145. Converting integer to binary number
146. Creating a directory and a file
147. Creating a file if not exists
148. Invoking a python file from another


