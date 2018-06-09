# 类内部的私有属性，需要在名字前加上__
# test在内部其实是_Student__test，如果我们在外面手动设置__test属性，这俩__test也不是同一个
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__test = "hello"
    def getName(self):
        return self.name
s1 = Student("ygy", "23")
s2 = Student("gyyin", "23")
s1.age = 10
print(s1.age)
print(s2.age)
print(type(s1))