# list, tuple, dict, set, str, generstor这些可以被for遍历的都是iterable
# iterable可以用 isstance来判断
from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance("ABC", Iterable))
print(isinstance((x*x for x in range(1, 11)), Iterable))
print(isinstance(100, Iterable))
# 能被next调用的称作iterator
# 同样用isstance判断
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance("ABC", Iterator))
print(isinstance((x*x for x in range(1, 11)), Iterator))
# 把list、tuple等变成iterator可以用iter方法
print(isinstance(iter([]), Iterator))