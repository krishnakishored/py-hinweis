import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    # x = threading.Thread(target=thread_function, args=(1,))

    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")

'''
11:19:46: Main    : before creating thread
11:19:46: Main    : before running thread
11:19:46: Thread 1: starting
11:19:46: Main    : wait for the thread to finish
11:19:46: Main    : all done  ### this line gets printed as last line if x.join() is used
11:19:48: Thread 1: finishing ### this line won't be printed if the thread is run as daemon

'''
