from functools import reduce

t = ['adam', 'LISA', 'barT']
def toUpper(str):
    l = len(str) - 1
    return str[0].upper() + str[1:l].lower()
print(list(map(toUpper, t)))

def prod(x, y):
    return x * y
print(reduce(prod, [1, 2, 3, 4]))

def str2float(str):
    MAP = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    def opr(x, y):
        if(y == "."):
            return x
        return x * 10 + MAP[y]
    l = len(str) - 1
    n = str.index(".")
    return reduce(opr, str, 0) / pow(10, l - n)
print(str2float("131234.56"))

def is_palindrome(s):
    str_n = str(s)
    return str_n[::-1] == str_n
print(is_palindrome(1234321))
