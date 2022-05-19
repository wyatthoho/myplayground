import time


def ShowTime(func):
    def wrapper(*args, **kw):
        timeStr = time.time()
        result = func(*args, **kw)
        timeEnd = time.time()
        print('Exec: {}, take {:2.1f} sec'.format(func.__name__, timeEnd - timeStr))
        return result
    return wrapper


@ShowTime
def SleepHalfSec():
    time.sleep(0.5)
    return 'done'


@ShowTime
def SleepOneSec():
    time.sleep(1.0)
    return 'done'


if __name__ == '__main__':
    SleepHalfSec()
    SleepOneSec()

