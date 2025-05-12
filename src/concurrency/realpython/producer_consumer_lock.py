import random
import logging
import concurrent.futures
import threading

SENTINEL = object()


def producer(pipeline):
    """
    Pretend we're getting a message from the network.
    # Producer-Consumer Using Lock
    """
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """
    The consumer reads a message from the pipeline and writes it to a fake db
    which in this case is just printing. If it gets the SENTINEL value,   
    it returns from the fn, which will terminate the thread.
    """
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    def __init__(self):
        '''
        __init__() initializes these three members and then calls .acquire() on the .consumer_lock. 
        This is the state you want to start in. 
        The producer is allowed to add a new message, but the consumer needs to wait until a message is present.
        '''
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        '''
        There’s something subtle going on in .get_message() that’s pretty easy to miss. 
        It might seem tempting to get rid of message and just have the fn end with return self.message.
        Ans: As soon as the consumer calls .producer_lock.release(), it can be swapped out, and the producer can start running.
        That could happen before .release() returns! This means that there is a slight possibility that when the function returns self.message,
        that could actually be the next message generated, so you would lose the first message. This is another example of a race condition.
        '''
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        return message

    def set_message(self, message, name):
        '''
        The producer will call this with a message. It will acquire
        the .producer_lock, set the .message, and the call .release()
        on then consumer_lock, which will allow the consumer to read that value
        '''
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)




if __name__ == "__main__":
    format = "(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)

    '''
    While it works for this limited test, 
    it is not a great solution to the producer-consumer problem in general
    because it only allows a single value in the pipeline at a time. 
    When the producer gets a burst of msgs, it will have nowhere to put them.
    '''