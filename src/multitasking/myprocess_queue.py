import multiprocessing
import time
from time import gmtime, strftime


def CookMeals(cookIdx, queue):
    while not queue.empty():
        meals = queue.get()

        msg = 'Cook {}: Start to cook. ({})'.format(cookIdx, strftime('%H:%M:%S', gmtime()))
        print(msg)

        cookTime = meals
        time.sleep(cookTime)

        msg = 'Cook {}: End of cooking. ({})'.format(cookIdx, strftime('%H:%M:%S', gmtime()))
        print(msg)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    
    orders = [8, 2, 5]

    my_queue = multiprocessing.Queue()
    for meals in orders:
        my_queue.put(meals)

    cook1 = multiprocessing.Process(target=CookMeals, args=(1, my_queue))
    cook2 = multiprocessing.Process(target=CookMeals, args=(2, my_queue))

    cook1.start()
    cook2.start()

    cook1.join()
    cook2.join()

