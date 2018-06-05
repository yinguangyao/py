L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
# 列表生成式
r1 = range(1, 11)
r2 = range(2, 12)
print([x * y for x in r1 for y in r2])
print([x + x for x in r1])
print([x for x in r1 if x % 2 == 0])
