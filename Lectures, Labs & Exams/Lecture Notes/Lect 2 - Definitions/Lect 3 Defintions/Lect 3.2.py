import time


def current_time():
    time_now = time.strftime("%H:%M:%S")
    # set the time now here inside the defintion as if outside at start of program the current time will be whatever time program started not current time.
    print("Current time is {}".format(time_now))


for i in range(5):
    current_time()

