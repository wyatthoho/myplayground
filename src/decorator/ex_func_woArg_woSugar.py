import time


def ShowTime(func):
    def wrapper(*args, **kw):
        timeStr = time.time()
        result = func(*args, **kw)
        timeEnd = time.time()
        print('Exec: {}, take {:2.1f} sec'.format(func.__name__, timeEnd - timeStr))
        return result
    return wrapper


def SleepHalfSec():
    time.sleep(0.5)
    return 'done'


def SleepOneSec():
    time.sleep(1.0)
    return 'done'


if __name__ == '__main__':
    SleepHalfSec = ShowTime(SleepHalfSec)
    SleepOneSec = ShowTime(SleepOneSec)

    SleepHalfSec()
    SleepOneSec()

