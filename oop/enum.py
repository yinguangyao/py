from enum import Enum
Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, month in Month.__members__.items():
    print(name, '=>', month, ',', month.value)