from functools import reduce

l = [1, 2, 3, 4]
def f(n):
    return n * n
print(map(f, l))
print(list(map(f, l)))
print(list(map(str, l)))
def add(x, y):
    return x + y
print(reduce(add, [1, 2, 3, 4, 5]))
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 2, 3, 4]))