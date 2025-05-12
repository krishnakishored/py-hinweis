from threading import Thread, Event
import time

# 12.1. Starting and Stopping Threads
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("T-minus", n)
            n -= 1
            time.sleep(2)


# threads defined via inheritance from the Thread class.
class CountdownThread(Thread):
    '''
    Although this works, it introduces an extra dependency between the code and the threading library.
    That is, you can only use the resulting code in the context of threads
    '''
    def __init__(self,n):
        super().__init__()
        self.n = 0

    def run(self):
        while self.n >0:
            print('T-minus',self.n)
            self.n=-1
            time.sleep(5)
    


if __name__ == "__main__":
    c = CountdownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()

    time.sleep(10)
    print('About to terminate')
    c.terminate() # Signal termination
    t.join() # Wait for actual termination (if needed)
    print('Terminated')

    # c2 = CountdownThread(5)
    # c2.start()



