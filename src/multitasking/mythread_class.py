import threading
import time
from time import gmtime, strftime


class MyThread(threading.Thread):
    def __init__(self, idx):
        threading.Thread.__init__(self)
        self.idx = idx

    def run(self):
        start = strftime('%H:%M:%S', gmtime())
        time.sleep(2)
        end = strftime('%H:%M:%S', gmtime())

        msg = 'Thread: {}, start: {}, end: {}'.format(self.idx, start, end)
        print(msg)


if __name__ == '__main__':
    timeStr = time.time()

    threads = [MyThread(i) for i in range(3)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
    timeEnd = time.time()
    print('Total time: {:.3f}s'.format(timeEnd - timeStr))

