# threading module
import time
from threading import Thread
import threading

import sys


def sleeper(i):
    print("thread %d sleeps for 5 seconds" % i)
    time.sleep(5)
    print("thread %d woke up" % i)


"""
Thread class: The class threading.Thread has a method start(), which can start a Thread.
It triggers off the method run(), which has to be overloaded.
The join() method makes sure that the main program waits until all threads have terminated.
"""


def our_decorator(func):
    def wrapper(x):
        print("before calling fn: " + func.__name__)
        func(x)
        print("after calling fn: " + func.__name__)

    return wrapper


@our_decorator
def sleeper_threads(n):
    for i in range(n):
        # sleeper(i)
        t = Thread(target=sleeper, args=(i,))
        t.start()


# using decorator type#1
# my_sleeper_threads = our_decorator(sleeper_threads)
# my_sleeper_threads(5)

# using decorator type#2 - using @our_decorator on function
sleeper_threads(3)


# ????? - Not Working
class PrimeNumber(threading.Thread):
    prime_numbers = {}
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number
        PrimeNumber.lock.acquire()
        PrimeNumber.prime_numbers[number] = "None"
        PrimeNumber.lock.release()

    def run(self):
        counter = 2
        res = True
        while counter * counter < self.Number and res:
            if self.Number % counter == 0:
                res = False
            counter += 1
        PrimeNumber.lock.acquire()
        PrimeNumber.prime_numbers[self.Number] = res
        PrimeNumber.lock.release()


def prime_numbers_threads():  # to run
    threads = []
    while True:
        # input = int(input("number: "))
        input1 = int(input("enter a number: "))
        if input1 < 1:
            break

        thread = PrimeNumber(input1)
        threads += [thread]
        thread.start()

    for x in threads:
        x.join()
