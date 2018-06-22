# os.path.split可以拆分路径，一部分是路径名，另一部分是文件名
# os.path.splitext可以获取到文件的扩展名，比如.txt
# os.rename可以对文件进行重命名
# os.remove可以删掉文件
import os
print("os's name is %s" % os.name)
print(os.path.abspath('.'))
p = os.path.join(os.path.abspath('.'), "test")
os.mkdir(p)
os.rmdir(p)
# os.rename("test.txt", "test111.txt")
s = [x for x in os.listdir(".") if os.path.isfile(x)]
print(s)
print(os.listdir(os.path.abspath(r"/Users/yinguangyao/Desktop/desktop/project/python")))
