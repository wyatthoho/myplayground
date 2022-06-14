import time


def PrintLoopState(tick, total, step=1):
    cond1 = tick % step == 0
    cond2 = tick == total
    
    if cond1 or cond2:
        action = True
    else:
        action = False

    if cond2:
        end = '\n'
    else:
        end = ''

    if action:
        progress = tick / total * 100
        msg = '{:.0f}/{:.0f} ({:.1f}%)'.format(tick, total, progress)
        print('\rRunning: ', msg, sep=' ', end=end)


if __name__ == '__main__':
    for itr in range(101):
        time.sleep(0.05)
        PrintLoopState(tick=itr+1, total=101, step=2)
    print('Done.')