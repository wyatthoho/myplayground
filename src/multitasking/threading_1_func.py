import threading
import time


def CookMeals(cookIdx, meals):
    msg = 'Cook {}: Start to cook.'.format(cookIdx)
    print(msg)

    cookTime = meals
    time.sleep(cookTime)

    msg = 'Cook {}: End of cooking. ({} meals)'.format(cookIdx, meals)
    print(msg)


if __name__ == '__main__':
    cook1 = threading.Thread(target=CookMeals, args=(1,8))
    cook2 = threading.Thread(target=CookMeals, args=(2,2))
    cook3 = threading.Thread(target=CookMeals, args=(3,5))

    cook1.start()
    cook2.start()
    cook3.start()

    cook1.join()
    cook2.join()
    cook3.join()

