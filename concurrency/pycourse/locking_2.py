#Re-entrant Locks
# Normal Lock objects cannot be acquired more than once, even by the same thread. 
# This can introduce undesirable side-effects if a lock is accessed by more than one function in the same call chain.

import threading,logging


def worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')


def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock aquired directly')    
    finally:
        lock.release()

if __name__=="__main__":
    lock = threading.Lock()

    print('First try :', lock.acquire())
    #the second call to acquire() is given a zero timeout to prevent it from blocking 
    # because the lock has been obtained by the first call.
    print('Second try:', lock.acquire(0)) # zero timeout

    # In a situation where separate code from the same thread needs to “re-acquire” the lock, use an RLock instead.

    rlock = threading.RLock()
    print('Third try :', rlock.acquire())
    print('Fourth try:', rlock.acquire(0))

    # Locks as Context Managers
    # Locks implement the context manager API and are compatible with the 'with' statement. 
    # Using with removes the need to explicitly acquire and release the lock.

    logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s',)

    lock_with = threading.Lock()
    w = threading.Thread(target=worker_with,args=(lock_with, ))
    nw = threading.Thread(target=worker_no_with,args=(lock_with, ))

    w.start()
    nw.start()

    