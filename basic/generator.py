# 如果在函数中使用了yield，那么这个函数就是一个generator
g = (x * x for x in range(1, 11))
# g1 = next(g)
# while not g1 is None:
#     print(g1)
#     g1 = next(g)
for n in g:
    print(n)