import time


def slow(callback, *args):
    print(args[1])
    time.sleep(3)
    return callback(*args)


def plus(a, b):
    return a + b


print(slow(plus, 1, 7))
