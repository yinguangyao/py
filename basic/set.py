# 和es6里面的set类似，接收一个list作为参数
# add可以添加，remove是移除
# &可以求交集，|可以求并集
s = set([1, 2, 3, 3])
print(s) # {1, 2, 3}
s.add(4);
print(s)
s.remove(3)
print(s)
test1 = set([1, 2, 3])
test2 = set([2, 3, 4])
print(test1 & test2)
print(test1 | test2)