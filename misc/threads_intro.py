



#thread.start_new_thread(function, args[, kwargs]) # starts a new thread and returns its identifier
from _thread import start_new_thread,allocate_lock

def heron(a):
    """Calculates the square root of a"""
    eps = 0.0000001
    old = 1
    new = 1
    while True:
        old,new = new, (new + a/new) / 2.0
        print (old, new)
        if abs(new - old) < eps:
            break
    return new

# start_new_thread(heron,(99,))
# start_new_thread(heron,(999,))
# start_new_thread(heron,(1733,))
# #c = raw_input("Type something to quit.")#The raw_input() in the previous example is necessary, because otherwise all the threads would be exited, if the main program finishes.
# c = input("Type something to quit.")

#expanding with counters - might not work as expected
'''
The problem arises by the assignments to num_thread
num_threads += 1 and num_threads -= 1
These assignment statements are not atomic.
'''

num_threads = 0
def heron_2(a):
    global num_threads
    num_threads += 1

    # code has been left out, see above
    eps = 0.0000001
    old = 1
    new = 1
    while True:
        old,new = new, (new + a/new) / 2.0
        print (old, new)
        if abs(new - old) < eps:
            break

    num_threads -= 1
    return new

# start_new_thread(heron_2,(99,))
# start_new_thread(heron_2,(999,))
# start_new_thread(heron_2,(1733,))
# start_new_thread(heron,(17334,))
#
# while num_threads > 0:
#     pass

#using lock is the solution
num_threads = 0
thread_started = False
lock = allocate_lock()
def heron(a):
    global num_threads, thread_started
    lock.acquire()
    num_threads += 1
    thread_started = True
    lock.release()

    eps = 0.0000001
    old = 1
    new = 1
    while True:
        old,new = new, (new + a/new) / 2.0
        print (old, new)
        if abs(new - old) < eps:
            break
    lock.acquire()
    num_threads -= 1
    lock.release()
    return new

start_new_thread(heron,(99,))
start_new_thread(heron,(999,))
start_new_thread(heron,(1733,))

while not thread_started:
    pass
while num_threads > 0:
    pass


'''

Threading :-
--------------
1) What is the difference between Process and Thread?
    A Thread or a Thread of Execution is defined in computer science as the smallest unit that can be scheduled in an operating system. Threads are normally created by a fork of a computer script or program in two or more parallel (which is implemented on a single processor by multitasking) tasks. Threads are usually contained in processes. More than one thread can exist within the same process. These threads share the memory and the state of the process. In other words: They share the code or instructions and the values of its variables.

    There are two different kind of threads:
    Kernel threads
    User-space Threads or user threads
    Kernel Threads are part of the operating system, while User-space threads are not implemented in the kernel.  A thread user-space thread is similar to a function or procedure call. But there are differences to regular functions, especially the return behaviour.

    Every process has at least one thread, i.e. the process itself. A process can start multiple threads. The operating system executes these threads like parallel "processes". On a single processor machine, this parallelism is achieved by thread scheduling or timeslicing.

2) What are the benefits of multi-threaded programming?
    Advantages of Threading:
    Multithreaded programs can run faster on computer systems with multiple CPUs, because theses threads can be executed truly concurrent.
    A program can remain responsive to input. This is true both on single and on multiple CPU
    Threads of a process can share the memory of global variables. If a global variable is changed in one thread, this change is valid for all threads. A thread can have local variables.

    The handling of threads is simpler than the handling of processes for an operating system. That's why they are sometimes called light-weight process (LWP)

3) What is difference between user Thread and daemon Thread?

4) What are the libraries in Python that support threads?
    There are two modules which support the usage of threads in Python: thread and threading
    Note: The thread module has been considered as "deprecated" for quite a long time. It has been renamed to "_thread" for backwards incompatibilities in Python3. The module "thread" treats a thread as a function, while the module "threading" is implemented in an object oriented way, i.e. every thread corresponds to an object.

5) Diffrenece between sleep() and wait() method ???
6) join() method use in python ??
7) What is synchronization?
8) Explain about Lock ?? and its two states(acquire and release??
9) What is Deadlock? How to analyze and avoid deadlock situation?
10) Explain about wait(),notify() and notifyALL() methods ??
      (Inter process comunication methods)
      (Thread condition mechanism)
11) Why wait(), notify() and notifyAll() methods have to be called from
      synchronized method or block?
12) What is the difference between threading.Lock and threading.RLock?
13) When and how to use Python's RLock??
14) How to terminate a blocking thread?
15) Can we start a thread twice ??

'''
