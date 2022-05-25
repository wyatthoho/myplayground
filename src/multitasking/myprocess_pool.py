import multiprocessing
import time
from time import gmtime, strftime


def CookMeals(cookIdx, meals):
    msg = 'Cook {}: Start to cook. ({})'.format(cookIdx, strftime('%H:%M:%S', gmtime()))
    print(msg)

    cookTime = meals
    time.sleep(cookTime)

    msg = 'Cook {}: End of cooking. ({})'.format(cookIdx, strftime('%H:%M:%S', gmtime()))
    print(msg)


if __name__ == '__main__':
    multiprocessing.freeze_support()

    pool = multiprocessing.Pool(3)

    pool.starmap(func=CookMeals, iterable=[(1, 8), (2, 2), (3, 5)])
    pool.close()

