import threading
import time
import queue

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
        threading.Thread.__init__(self)
        self.cookIdx = cookIdx
        self.queue = queue
        self.lock = lock

    def run(self):
        while not self.queue.empty():
            order = self.queue.get()
            orderIdx, meal = order.values()
            cookTime = meal / 10

            print(f'Lock state before Cook {self.cookIdx} acquired: {self.lock.locked()}')
            self.lock.acquire()
            print(f'Lock state after Cook {self.cookIdx} acquired: {self.lock.locked()}')

            msg = f'Order {orderIdx} is assigned to Cook {self.cookIdx}.'
            print(msg)

            time.sleep(cookTime)
            msg = f'Order {orderIdx} is done.'
            print(msg)

            print(f'Lock state before Cook {self.cookIdx} release: {self.lock.locked()}')
            self.lock.release()
            print(f'Lock state after Cook {self.cookIdx} release: {self.lock.locked()}')


orders = [{'idx': 1, 'meal': 8},
          {'idx': 2, 'meal': 2},
          {'idx': 3, 'meal': 5}]


my_queue = queue.Queue()
for order in orders:
    my_queue.put(order)

lock = threading.Lock()

cook1 = Cook(cookIdx=1, queue=my_queue, lock=lock)
cook2 = Cook(cookIdx=2, queue=my_queue, lock=lock)

cook1.start()
cook2.start()

cook1.join()
cook2.join()

