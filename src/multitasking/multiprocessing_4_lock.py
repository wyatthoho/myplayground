import multiprocessing
import time


class Cook(multiprocessing.Process):
    def __init__(self, cookIdx, queue, lock):
        super().__init__()
        self.cookIdx = cookIdx
        self.queue = queue
        self.lock = lock

    def run(self):
        while not self.queue.empty():
            meals = self.queue.get()
            self.lock.acquire()

            msg = 'Cook {}: Start to cook.'.format(self.cookIdx)
            print(msg)

            cookTime = meals
            time.sleep(cookTime)

            msg = 'Cook {}: End of cooking. ({} meals)'.format(self.cookIdx, meals)
            print(msg)
            self.lock.release()


if __name__ == '__main__':
    orders = [8, 2, 5]

    my_queue = multiprocessing.Queue()
    for meals in orders:
        my_queue.put(meals)

    lock = multiprocessing.Lock()

    cook1 = Cook(cookIdx=1, queue=my_queue, lock=lock)
    cook2 = Cook(cookIdx=2, queue=my_queue, lock=lock)

    cook1.start()
    cook2.start()

    cook1.join()
    cook2.join()

