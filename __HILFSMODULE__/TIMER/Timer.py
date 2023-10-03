import time


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(10)
        num_of_secs -= 1

    print('Countdown finished.')


def countdown_2_():
    sec = 3
    while sec >= 0:
        time.sleep(1)
        sec -= 1
        print(sec)

countdown_2_()

