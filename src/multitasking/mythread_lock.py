import threading
import time
import queue
from time import gmtime, strftime

'''
When the state is unlocked, 
    acquire() changes the state to locked 
    and returns immediately. 

When the state is locked, 
    acquire() blocks until a call to release() 
    in another thread changes it to unlocked, 
    then the acquire() call resets it to locked 
    and returns.
'''

'''
Queue.get(block=True, timeout=None)
    if block is true and timeout is None, 
    this operation goes into an uninterruptible wait 
    on an underlying lock. 
'''

class Cook(threading.Thread):
    def __init__(self, cookIdx, queue, lock):
        super().__init__()
        self.cookIdx = cookIdx
        self.queue = queue
        self.lock = lock

    def run(self):
        while not self.queue.empty():
            meals = self.queue.get()
            self.lock.acquire()

            msg = 'Cook {}: Start to cook. ({})'.format(self.cookIdx, strftime('%H:%M:%S', gmtime()))
            print(msg)

            cookTime = meals
            time.sleep(cookTime)

            msg = 'Cook {}: End of cooking. ({})'.format(self.cookIdx, strftime('%H:%M:%S', gmtime()))
            print(msg)
            self.lock.release()


if __name__ == '__main__':
    orders = [8, 2, 5]

    my_queue = queue.Queue()
    for meals in orders:
        my_queue.put(meals)

    lock = threading.Lock()

    cook1 = Cook(cookIdx=1, queue=my_queue, lock=lock)
    cook2 = Cook(cookIdx=2, queue=my_queue, lock=lock)

    cook1.start()
    cook2.start()

    cook1.join()
    cook2.join()

