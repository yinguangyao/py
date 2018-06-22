# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class screen(object):
    def __init__(self):
        self.__width = 100
        self.__height = 200
    @property
    def height(self):
        return self.__height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
s = screen()
print(s.height)
print(s.width)
s.width = 10
s.height = 20
print(s.width)
