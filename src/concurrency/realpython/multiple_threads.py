import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     threads = list()
#     for index in range(3):
#         logging.info("Main    : create and start thread %d.", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()

#     for index, thread in enumerate(threads):
#         logging.info("Main    : before joining thread %d.", index)
#         thread.join()
#         logging.info("Main    : thread %d done", index)

'''
11:42:50: Main    : create and start thread 0.
11:42:50: Thread 0: starting
11:42:50: Main    : create and start thread 1.
11:42:50: Thread 1: starting
11:42:50: Main    : create and start thread 2.
11:42:50: Thread 2: starting
11:42:50: Main    : before joining thread 0.
11:42:52: Thread 0: finishing
11:42:52: Thread 1: finishing
11:42:52: Thread 2: finishing
11:42:52: Main    : thread 0 done
11:42:52: Main    : before joining thread 1.
11:42:52: Main    : thread 1 done
11:42:52: Main    : before joining thread 2.
11:42:52: Main    : thread 2 done


The order in which threads are run is determined by the operating system and can be quite hard to predict. 
It may (and likely will) vary from run to run, so you need to be aware of that when you design algorithms that use threading
'''

# Using a ThreadPoolExecutor

import concurrent.futures

# The easiest way to create it is as a context manager, 
# using the with statement to manage the creation and destruction of the pool.



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))

    '''
    The code creates a ThreadPoolExecutor as a context manager, telling it how many worker threads it wants in the pool. It then uses .map() to step through an iterable of things, in your case range(3), passing each one to a thread in the pool.

    The end of the with block causes the ThreadPoolExecutor to do a .join() on each of the threads in the pool. It is strongly recommended that you use ThreadPoolExecutor as a context manager when you can so that you never forget to .join() the threads.
    '''       