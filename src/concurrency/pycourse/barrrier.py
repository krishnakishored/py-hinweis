# Barriers are another thread synchronization mechanism. 
# A Barrier establishes a control point and all participating threads block until all of the participating “parties” have reached that point. 
# It lets threads start up separately and then pause until they are all ready to proceed.

import threading,time

def worker(barrier):
    print(threading.current_thread().getName(),'waiting for barrier with {} others'.format(barrier.n_waiting))
    worker_id = barrier.wait()
    print(threading.current_thread().name,'after barrier',worker_id)

def worker_2(barrier):
    print(threading.current_thread().name,
          'waiting for barrier with {} others'.format(
              barrier.n_waiting))
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, 'aborting')
    else:
        print(threading.current_thread().name, 'after barrier',
              worker_id)

NUM_THREADS = 3

if __name__=="__main__":
    barrier = threading.Barrier(NUM_THREADS)
    threads = [
        threading.Thread(name="worker-%s" % i,target=worker,args=(barrier, )) for i in range(NUM_THREADS)
    ] # using list comprehension

    for t in threads:
        print(t.name,'Starting')
        t.start()
        time.sleep(0.1)

    for t in threads:
        t.join()        

    # In this example, the Barrier is configured to block until three threads are waiting. 
    # When the condition is met, all of the threads are released past the control point at the same time. 
    # The return value from wait() indicates the number of the party being released, and can be used to limit some threads from taking an action like cleaning up a shared resource.
    barrier2 = threading.Barrier(NUM_THREADS + 1)
    
    threads2 = [threading.Thread(name='worker2-%s' % i,target=worker_2,args=(barrier2,),) for i in range(NUM_THREADS)]
    
    for t in threads2:
        print(t.name,'starting')
        t.start()
        time.sleep(1)
    
    barrier2.abort()   
    
    for t in threads2:
        t.join() 




