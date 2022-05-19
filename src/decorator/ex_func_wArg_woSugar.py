import time


def ShowTime(showName: bool):
    def wrapperOuter(func):
        def wrapperInner(*args, **kw):
            timeStr = time.time()
            result = func(*args, **kw)
            timeEnd = time.time()
            if showName:
                print('Exec: {}, take {:2.1f} sec'.format(func.__name__, timeEnd - timeStr))
            else:
                print('Take {:2.1f} sec'.format(timeEnd - timeStr))
            return result
        return wrapperInner
    return wrapperOuter


def SleepHalfSec():
    time.sleep(0.5)
    return 'done'


def SleepOneSec():
    time.sleep(1.0)
    return 'done'


if __name__ == '__main__':
    SleepHalfSec = ShowTime(showName=False)(SleepHalfSec)
    SleepOneSec = ShowTime(showName=True)(SleepOneSec)

    SleepHalfSec()
    SleepOneSec()

