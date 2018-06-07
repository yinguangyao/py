# 本质上是一个高阶函数
import functools
import time
# 如果我们想在运行now的时候，打印前做一些处理，该怎么办呢
def log(text):
    def decorator(func):
        # 这一句相当于 wrapped.__name__ = func.__name__
        @functools.wraps(func)
        def wrapped(*args):
            print("before and this is %s" % text)
            return func(*args)
        return wrapped
    return decorator
@log("test")
def now():
    print("2018-06-07")
now()
print(now.__name__)
#练习：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    @functools.wraps(fn)
    def wrapped(*args):
        start = time.time()
        result = fn(*args)
        timeInterval = time.time() - start
        print("timeInterval is %fs" % timeInterval)
        return result
    return wrapped

@metric
def test():
    for i in range(0, 1000):
        pass
test()
print(test.__name__)