# Python’s built-in data structures (lists, dictionaries, etc.) are thread-safe as a side-effect of having atomic byte-codes for manipulating them 
# (the global interpreter lock used to protect Python’s internal data structures is not released in the middle of an update). 
# Other data structures implemented in Python, or simpler types like integers and floats, do not have that protection. 
# To guard against simultaneous access to an object, use a Lock object.

import logging,time,threading,random

class Counter:
    def __init__(self,start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value+1
        finally:
            self.lock.release()            

def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f',pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')    

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)    



# To find out whether another thread has acquired the lock without holding up the current thread, pass False for the blocking argument to acquire().
# In the next example, worker() tries to acquire the lock three separate times and counts how many attempts it has to make to do so.
# In the mean time, lock_holder() cycles between holding and releasing the lock, with short pauses in each state used to simulate load.


def lock_holder(lock):
    logging.debug('Starting')
    while True:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(0.2)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(0.5)


def worker_2(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires <3:
        logging.debug('Trying to acquire')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: acquired', num_tries)
                num_acquires +=1
            else:
                logging.debug('Iteration %d: Not acquired',num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug('Done after %d iterations', num_tries)




if __name__=="__main__":
    # counter = Counter()
    # for i in range(2):
    #     t=threading.Thread(target=worker,args=(counter,))
    #     t.start()

    # logging.debug('Waiting for worker threads')    
    # main_thread = threading.main_thread()
    # for t in threading.enumerate():
    #     if t is not main_thread:
    #         t.join()
    # logging.debug('Counter:%d',counter.value)        


    lock = threading.Lock()
    holder = threading.Thread(target=lock_holder,args=(lock,),name="lockHolder",daemon=True)
    holder.start()

    worker_2 = threading.Thread(target=worker_2,args=(lock,),name="worker_2")
    worker_2.start()

#In this example, the worker() function increments a Counter instance, which manages a Lock to prevent two threads from changing its internal state at the same time. 
# If the Lock was not used, there is a possibility of missing a change to the value attribute.

