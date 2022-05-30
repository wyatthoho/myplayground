import multiprocessing
import time
from time import gmtime, strftime


class Cook(multiprocessing.Process):
    def __init__(self, cookIdx, meals, conn1, conn2):
        super().__init__()
        self.cookIdx = cookIdx
        self.meals = meals
        self.conn1 = conn1
        self.conn2 = conn2

    def run(self):
        msg = 'Cook {}: Start to cook. ({})'.format(self.cookIdx, strftime('%H:%M:%S', gmtime()))
        print(msg)

        if self.meals > 6:
            sendMeals = 1
            self.meals -= sendMeals
            self.conn1.send({'Cook': self.cookIdx, 'sendMeals': sendMeals})

        elif self.conn2.poll():
            recvMeals = self.conn2.recv()['sendMeals']
            self.meals += recvMeals
        
        cookTime = self.meals
        time.sleep(cookTime)

        msg = 'Cook {}: End of cooking. ({})'.format(self.cookIdx, strftime('%H:%M:%S', gmtime()))
        print(msg)


if __name__ == '__main__':
    multiprocessing.freeze_support()

    conn1, conn2 = multiprocessing.Pipe()
    cook1 = Cook(cookIdx=1, meals=8, conn1=conn1, conn2=conn2)
    cook2 = Cook(cookIdx=2, meals=2, conn1=conn1, conn2=conn2)
    cook3 = Cook(cookIdx=3, meals=5, conn1=conn1, conn2=conn2)

    cook1.start()
    cook2.start()
    cook3.start()

    cook1.join()
    cook2.join()
    cook3.join()

