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


def test():
    print('start')
    while True:
        x = yield
        print('значение: ', x)


g = test()
next(g)
g.send('yyyyy')
