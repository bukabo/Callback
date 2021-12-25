from time import time


def gen(s):
    for i in s:
        yield i


def gen_time():
    while True:
        pattern = 'time-{}'
        t = int(time() * 1000)

        yield pattern.format(str(t))

        print('hi')

        yield 2


g = gen_time()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
