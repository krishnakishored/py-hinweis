# Thread-specific Data
# While some resources need to be locked so multiple threads can use them, others need to be protected so that they are hidden from threads that do not own them. 
# The local() class creates an object capable of hiding values from view in separate threads


import random, threading, logging


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)

def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s',)

# To initialize the settings so all threads start with the same value, use a subclass and set the attributes in __init__().

class MyLocal(threading.local):
    def __init__(self,value):
        super().__init__()
        logging.debug('Initializing %r', self)
        self.value = value


if __name__=="__main__":
    # The attribute local_data.value is not present for any thread until it is set in that thread.

    local_data = threading.local()
    show_value(local_data)
    local_data.value = 1000
    show_value(local_data)

    for i in range(2):
        t = threading.Thread(target=worker, args=(local_data,))
        t.start()

    # __init__() is invoked on the same object (note the id() value), once in each thread to set the default values.
    local_data_2 = MyLocal(1000)
    show_value(local_data_2)

    for i in range(2):
        t = threading.Thread(target=worker, args=(local_data_2,))
        t.start()
