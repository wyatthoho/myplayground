import time
import threading
import queue

class Worker(threading.Thread):
    def __init__(self, queue, num, semaphore):
        threading.Thread.__init__(self)
        self.queue = queue
        self.num = num
        self.semaphore = semaphore

    def run(self):
        while self.queue.qsize() > 0:
            msg = self.queue.get()

            # 取得旗標
            semaphore.acquire()
            print("Semaphore acquired by Worker %d" % self.num)

            # 僅允許有限個執行緒同時進的工作
            print("Worker %d: %s" % (self.num, msg))
            time.sleep(1)

            # 釋放旗標
            print("Semaphore released by Worker %d" % self.num)
            self.semaphore.release()

my_queue = queue.Queue()
for i in range(5):
    my_queue.put("Data %d" % i)

# 建立旗標
semaphore = threading.Semaphore(2)

my_worker1 = Worker(my_queue, 1, semaphore)
my_worker2 = Worker(my_queue, 2, semaphore)
my_worker3 = Worker(my_queue, 3, semaphore)

my_worker1.start()
my_worker2.start()
my_worker3.start()

my_worker1.join()
my_worker2.join()
my_worker3.join()

print("Done.")