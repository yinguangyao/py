# 实际上，len函数调用的时候会手动调用内部的__len__方法
class MyDog(object):
    def __len__(self):
        return 100
    def __test__(self):
        return "test"
dog = MyDog()
print(len(dog))
print(hasattr(dog, '__test__'))
setattr(dog, "attr", "test")
print(dog.attr);
# 可以设置一下，如果不存在test属性就默认返回404
print(getattr(dog, "test", 404))