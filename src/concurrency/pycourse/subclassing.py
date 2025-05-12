# At start-up, a Thread does some basic initialization and then calls its run() method, which calls the target function passed to the constructor. 
# To create a subclass of Thread, override run() to do whatever is necessary.

import threading,logging,time

class MyThread(threading.Thread):

    def run(self):
        # logging.debug('running: {}'.format(threading.current_thread().getName()))
        logging.debug(' running')





# Because the args and kwargs values passed to the Thread constructor are saved in private variables using names prefixed with '__', they are not easily accessed from a subclass. 
# To pass arguments to a custom thread type, redefine the constructor to save the values in an instance attribute that can be seen in the subclass.

class MyThreadWithArgs(threading.Thread):
    def __init__(self,group=None,target=None,name=None,args=(),kwargs=None,*,daemon=None):
        super().__init__(group=group,target=target,name=name,daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running with {} and {}'.format(self.args,self.kwargs))




logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-7s) %(message)s',
)



# One example of a reason to subclass Thread is provided by Timer, also included in threading. 
# A Timer starts its work after a delay, and can be canceled at any point within that delay time period.

def delayed():
    logging.debug('worker running')

if __name__=="__main__":
    for i in range(5):
        t1=MyThread(name="t-"+str(i))
        t2 = MyThreadWithArgs(args=(i,), kwargs={'a': 'A', 'b': 'B'})

        t1.start()
        t2.start()

        t3=threading.Timer(3,delayed)
        t3.setName('t3')
        t4=threading.Timer(5,delayed)
        t4.setName('t4')
        
        logging.debug('Starting Timers')
        t3.start()
        t4.start()

        logging.debug('waiting before canceling %s', t4.getName())
        time.sleep(0.2)
        logging.debug('canceling %s', t4.getName())
        t4.cancel()
        logging.debug('done')


