import threading,time,logging

import random

# Sometimes programs spawn a thread as a daemon that runs without blocking the main program from exiting. 


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


def worker():
    """thread worker function"""
    pause = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

if __name__=="__main__":
    d=threading.Thread(name='daemon',target=daemon,daemon=True)
    t=threading.Thread(name='non-daemon',target=non_daemon)

    d.start()
    t.start()#The output does not include the "Exiting" message from the daemon thread,

    # To wait until a daemon thread has completed its work, use the join() method.
    # d.join()
    # t.join()

    # By default, join() blocks indefinitely. It is also possible to pass a float value representing the number of seconds to wait for the thread to become inactive. If the thread does not complete within the timeout period, join() returns anyway.
    d.join(0.5)
    # d.join(0.1)# d.isAlive() True
    print('d.isAlive()', d.isAlive())
    t.join()

    # Enumerating All Threads
    # It is not necessary to retain an explicit handle to all of the daemon threads in order to ensure they have completed before exiting the main process.
    # enumerate() returns a list of active Thread instances. 
    # The list includes the current thread, and since joining the current thread introduces a deadlock situation, it must be skipped.

    for i in range(3):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
    
    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue  # joining the current thread introduces deadlock
        logging.debug('joining %s', t.getName())
        t.join()
