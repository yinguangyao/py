# 如果是0，那么可以省略，比如list[:10]是取前10个，list[-10:]取的是后十个
# 这两个都是索引，获取第一个到第三个
list = [1, 2, 3, 4]
t = (1, 2, 3, 4)
str = "hello, world"
print(str[1:3])
print(t[1:2])
print(list[1:3])
# 前4个数每两个选一个
print(list[:4:2])