# 一般在函数中需要进行类型判断，对不符合的类型进行报错
# 函数可以一次返回多个值
# 调用的时候传入参数个数不一致会报错
def add(a, b):
    if(not isinstance(a, (int, float)) or not isinstance(b, (int, float))):
        raise TypeError("bad operand type")
    return a + b;
print(add(1, 2))
# 这里返回的其实是一个tuple类型
def opr(a, b):
    return a+b, a-b
print(opr(10, 20))
count = 1
def addCount():
    a = count
    print(a)
addCount()