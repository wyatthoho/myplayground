import multiprocessing
import time
from time import gmtime, strftime


class Cook(multiprocessing.Process):
    def __init__(self, cookIdx, meals):
        super().__init__()
        self.cookIdx = cookIdx
        self.meals = meals

    def run(self):
        msg = 'Cook {}: Start to cook. ({})'.format(self.cookIdx, strftime('%H:%M:%S', gmtime()))
        print(msg)

        cookTime = self.meals
        time.sleep(cookTime)

        msg = 'Cook {}: End of cooking. ({})'.format(self.cookIdx, strftime('%H:%M:%S', gmtime()))
        print(msg)


if __name__ == '__main__':
    multiprocessing.freeze_support()

    cook1 = Cook(cookIdx=1, meals=8)
    cook2 = Cook(cookIdx=2, meals=2)
    cook3 = Cook(cookIdx=3, meals=5)

    cook1.start()
    cook2.start()
    cook3.start()

    cook1.join()
    cook2.join()
    cook3.join()

