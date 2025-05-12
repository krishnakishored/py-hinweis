from threading import Thread, Event, Condition, Semaphore
import time

# Code to execute in an independent thread
def countdown_1(n, started_evt):
    print("countdown_1 starting")
    started_evt.set() 
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(2)
###############################################################

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        # self._cv = threading.Condition()
        self._cv = Condition()


    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        '''
        Run the timer and notify waiting threads after each interval
        '''
        while True:
            time.sleep(self._interval)
            with self._cv:
                 self._flag ^= 1
                 self._cv.notify_all()

    def wait_for_tick(self):
        '''
        Wait for the next tick of the timer
        '''
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()



###############################################################

# Worker thread
def worker(n, sema):
    # Wait to be signalled
    sema.acquire()
    # Do some work
    print("Working", n)



###############################################################
'''
When you run this code, the “countdown_1 is running” message will always appear after the “countdown_1 starting” message. 
This is coordinated by the event that makes the main thread wait until the countdown_1() function has first printed the startup message.
'''
if __name__ == "__main__":
###############################################################
    # # Create the event object that will be used to signal startup
    # started_evt = Event()    
    # # 12.2. Determining If a Thread Has Started
    # # Launch the thread and pass the startup event
    # print("Launching the countdown_1")
    # t2 = Thread(target=countdown_1, args=(10,started_evt))
    # t2.start()

    # #wait for the thread to start
    # started_evt.wait()
    # print("countdown_1 is running")
###############################################################

    # # Example use of the timer
    # ptimer = PeriodicTimer(5)
    # ptimer.start()

    # # Two threads that synchronize on the timer
    # def countdown(nticks):
    #     while nticks > 0:
    #         ptimer.wait_for_tick()
    #         print("T-minus", nticks)
    #         nticks -= 1

    # def countup(last):
    #     n = 0
    #     while n < last:
    #         ptimer.wait_for_tick()
    #         print("Counting", n)
    #         n += 1

    # Thread(target=countdown, args=(10,)).start()
    # Thread(target=countup, args=(5,)).start()
###############################################################

    # Create some threads
    sema = Semaphore(0)
    nworkers = 10
    for n in range(nworkers):
        t3 = Thread(target=worker, args=(n, sema,))
        t3.daemon=True
        t3.start()

    print('About to release first worker')
    time.sleep(5)
    sema.release()
    time.sleep(1)
    print('About to release second worker')
    time.sleep(5)
    sema.release()
    time.sleep(1)
    '''
    If you run this, a pool of threads will start, but nothing happens because they’re all blocked waiting to acquire the semaphore. 
    Each time the semaphore is released, only one worker will wake up and run.
    '''
    
    # print('About to release third worker')
    # time.sleep(5)
    # sema.release()
    # time.sleep(1)
    # print('About to release fourth worker')
    # time.sleep(5)
    # sema.release()
    # time.sleep(1)
    print('Goodbye')


###############################################################