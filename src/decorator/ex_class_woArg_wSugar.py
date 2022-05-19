import time


class ShowTime:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kw):
        timeStr = time.time()
        result = self.func(*args, **kw)
        timeEnd = time.time()
        print('Exec: {}, take {:2.1f} sec'.format(self.func.__name__, timeEnd - timeStr))
        return result


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

