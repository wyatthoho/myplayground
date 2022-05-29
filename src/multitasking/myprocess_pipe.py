import multiprocessing
import time
from time import gmtime, strftime


def CookMeals(cookIdx, meals, conn1, conn2):
    msg = 'Cook {}: Start to cook. ({})'.format(cookIdx, strftime('%H:%M:%S', gmtime()))
    print(msg)

    if meals > 6:
        sendMeals = 1
        meals -= sendMeals
        conn1.send({'Cook': cookIdx, 'sendMeals': sendMeals})
        conn1.close()

    elif conn2.poll():
        recvMeals = conn2.recv()['sendMeals']
        meals += recvMeals
        conn2.close()
    
    cookTime = meals
    time.sleep(cookTime)

    msg = 'Cook {}: End of cooking. ({})'.format(cookIdx, strftime('%H:%M:%S', gmtime()))
    print(msg)


if __name__ == '__main__':
    multiprocessing.freeze_support()

    conn1, conn2 = multiprocessing.Pipe()
    cook1 = multiprocessing.Process(target=CookMeals, args=(1, 8, conn1, conn2))
    cook2 = multiprocessing.Process(target=CookMeals, args=(2, 2, conn1, conn2))
    cook3 = multiprocessing.Process(target=CookMeals, args=(3, 5, conn1, conn2))

    cook1.start()
    cook2.start()
    cook3.start()

    cook1.join()
    cook2.join()
    cook3.join()

