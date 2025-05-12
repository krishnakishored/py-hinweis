from queue import Queue
from threading import Thread
import time

_sentinel = object()

# A thread that produces data
def producer(out_q):
    n = 10
    while n > 0:
        # Produce some data
        out_q.put(n)
        time.sleep(2)
        n -= 1


    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()

        # Check for termination
        '''
        A subtle feature of this example is that the consumer, upon receiving the special sentinel value, immediately places it back onto the queue. 
        This propagates the sentinel to other consumers threads that might be listening on the same queue—thus shutting them all down one after the other.
        '''
        if data is _sentinel:
            in_q.put(_sentinel)
            break

        # Process the data
        print('Got:', data)
    print('Consumer shutting down')

if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    