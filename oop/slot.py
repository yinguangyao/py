# slots可以限制当前类的实例只能设置哪些属性
# 但是对继承的子类无效
class Student(object):
    __slots__ = ["name", "age"]
s1 = Student()
s1.name = "111"
s1.age = 20
s1.sex = "female"
