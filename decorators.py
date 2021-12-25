from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

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
    l = [x for x in range(n) if x % 2 == 0]
    return l

@timeit
def fib(x):
    return fib(x - 1) + fib(x - 2) if x > 1 else x




# one(10 ** 4)
# print(two(10 ** 4))
ff=fib(10)
print(ff)
