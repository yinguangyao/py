# 可以配合range方法遍历索引
# range会创建一个长度为传入数字的list
# range(5)为0,1,2,3,4
# while ... else语法
# pass是占位符，py里面如果是if或者函数中，不能什么都不写，所以这个时候可以用pass
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hello, %s" % name);
# 如果想要循环遍历下标，有两种方式
# 第一种
length = len(L) - 1
index = 0
while index <= length:
    print("hello, %s" % L[index])
    index = index + 1
for i in range(len(L)):
    print(L[i])
# 第二种
for i, value in enumerate(L):
    print("value is: %s" % value)
for x, y in [(1, 2), (2, 4), (3, 6)]:
    print(x, y)