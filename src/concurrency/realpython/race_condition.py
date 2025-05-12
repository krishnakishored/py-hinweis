import logging
import threading
import time
import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        '''
        It’s simulating reading a value from a database, 
        doing some computation on it, 
        and then writing a new value back to the database.
        '''
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    # You can turn on full logging by setting the level to DEBUG by adding
    #  this statement after you configure the logging output in __main__:
    # logging.getLogger().setLevel(logging.DEBUG)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            # # .submit(function, *args, **kwargs)
            # 11:19:04: Testing update. Ending value is 2.
            executor.submit(database.locked_update, index)
            # 11:02:11: Testing update. Ending value is 1.
            # executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)

# def inc(x):
#     x += 1

# if __name__ == "__main__":
#     import dis
#     dis.dis(inc)
#  
# The REPL example uses dis from the Python standard library
# to show the smaller steps that the processor does to implement your function.
#  25           0 LOAD_FAST                0 (x)
#               2 LOAD_CONST               1 (1)
#               4 INPLACE_ADD
#               6 STORE_FAST               0 (x)
#               8 LOAD_CONST               0 (None)
#              10 RETURN_VALUE
