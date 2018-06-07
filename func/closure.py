# 类似js中的闭包
# 和js中的for循环坑一样
def test():
    list = [1, 2, 3]
    fs = []
    for i in list:
        def f():
            return i
        fs.append(f)
    return fs
# 这里输出全部是3，熟悉JS的自然懂
for f in test():
    print(f())
# 如果需要避免这种情况该怎么办？JS中可以用立即执行函数
def test1():
    list = [1, 2, 3]
    fs = []
    for i in list:
        def f1(j):
            def f():
                return j
            return f
        fs.append(f1(i))
    return fs
for f1 in test1():
    print(f1())
# 练习题
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    count = 0
    def counter():
        nonlocal count
        count = count + 1
        return count
    return counter
counter = createCounter()
print(counter())
print(counter())
print(counter())