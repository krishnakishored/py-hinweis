import threading
import time
import logging

def worker():
    """ thread worker func """
    print('worker')

def worker_arg(num):
    print("worker: {}".format(num))

def worker_names():
    print(threading.current_thread().getName(),'Starting')
    time.sleep(0.2)
    print(threading.current_thread().getName(),'Exiting')

def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.3)
    print(threading.current_thread().getName(), 'Exiting')


def worker_log():
    logging.debug('Starting')
    time.sleep(0.5)
    logging.debug('Exiting')


def my_service_log():
    logging.debug('Starting')
    time.sleep(0.3)
    logging.debug('Exiting')


if __name__=="__main__":
    threads = []
 
    # for i in range(5):
    #     t = threading.Thread(target=worker, args=(i,))
    #     threads.append(t)
    #     t.start()

    w2 = threading.Thread(target=worker_names)  # use default name # Thread-1 
    w = threading.Thread(name="worker_named",target=worker_names)
    t = threading.Thread(name='my_service', target=my_service)

    w.start()
    w2.start()
    t.start()
    
    w4 = threading.Thread(target=worker_log)  # use default name # Thread-1 
    w3 = threading.Thread(name="worker_named",target=worker_log)
    t2 = threading.Thread(name='my_service', target=my_service_log)
    logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-10s) %(message)s')
    w3.start()
    t2.start()
    w4.start()


