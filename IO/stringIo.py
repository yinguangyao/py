# 看起来readlines是无法读取只有一行的内容的
from io import StringIO
f1 = StringIO()
f2 = StringIO()
f3 = StringIO("hello, \nworld")
f1.write("hello")
f2.write("world")
print(f1.getvalue())
print(f2.getvalue())
print(f3.read())
for line in f3.readlines():
    print(line.strip())