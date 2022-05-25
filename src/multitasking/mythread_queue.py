import threading
import time
import queue


class Cook(threading.Thread):
    def __init__(self, cookIdx, queue):
        threading.Thread.__init__(self)
        self.cookIdx = cookIdx
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            order = self.queue.get()
            orderIdx, meal = order.values()
            cookTime = meal / 10

            msg = f'Order {orderIdx} is assigned to Cook {self.cookIdx}.'
            print(msg)

            time.sleep(cookTime)
            msg = f'Order {orderIdx} is done.'
            print(msg)


if __name__ == '__main__':
    timeStr = time.time()

    orders = [{'idx': 1, 'meal': 8},
              {'idx': 2, 'meal': 2},
              {'idx': 3, 'meal': 5}]

    my_queue = queue.Queue()
    for order in orders:
        my_queue.put(order)

    cook1 = Cook(cookIdx=1, queue=my_queue)
    cook2 = Cook(cookIdx=2, queue=my_queue)

    cook1.start()
    cook2.start()

    cook1.join()
    cook2.join()

    timeEnd = time.time()
    print('Total time: {:.3f}s'.format(timeEnd - timeStr))

