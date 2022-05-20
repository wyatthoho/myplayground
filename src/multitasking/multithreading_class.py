import os
import threading
import time


class Sleep(threading.Thread):
    def __init__(self, sleep_duration) -> None:
        self.sleep_duration = sleep_duration
    
    def sleep(self):
        time.sleep(self.sleep_duration)


if __name__ == "__main__":
    time_start = time.time()

    # Create thread
    sleep_class = Sleep(2)
    t1 = threading.Thread(target=sleep_class.sleep)

    # Start task execution
    t1.start()

    # Wait for thread to complete execution
    t1.join()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")