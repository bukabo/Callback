from datetime import datetime
from time import sleep


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        # result = func(*args, **kwargs)

        print('Время выполнения: ' + str(datetime.now() - start).split('.')[0])
        return func(*args, **kwargs)  # result

    return wrapper


@timeit
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@timeit
def two(n):
    sleep(2)
    l = [print(x) for x in range(n) if x % 2 == 0]
    print("end func 'two'")
    return l


@timeit
def fib(x):
    return fib(x - 1) + fib(x - 2) if x > 1 else x


# one(10 ** 4)
# print(two(10 ** 4))
ff = two(10)

# two(20)
# print(ff)
