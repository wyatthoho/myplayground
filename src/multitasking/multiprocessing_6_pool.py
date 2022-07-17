import multiprocessing
import time


def CookMeals(cookIdx, meals):
    msg = 'Cook {}: Start to cook.'.format(cookIdx)
    print(msg)

    cookTime = meals
    time.sleep(cookTime)

    msg = 'Cook {}: End of cooking. ({} meals)'.format(cookIdx, meals)
    print(msg)


if __name__ == '__main__':
    multiprocessing.freeze_support()

    pool = multiprocessing.Pool(3)
    pool.starmap(func=CookMeals, iterable=[(1, 8), (2, 2), (3, 5)])
    pool.close()

