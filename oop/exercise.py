# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
# 这个count应该类似于js中的类属性，直接用Student.count设置的
class Student(object):
    count = 0

    def __init__(self, name):
        Student.count += 1
        self.name = name
s1 = Student("ygy")
s2 = Student("gyyin")
s3 = Student("3")

print(Student.count)