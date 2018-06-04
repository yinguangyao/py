# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(list):
    # if(not isinstance(list, list)):
    #     raise TypeError("bad type")
    min = list[0]
    max = list[0]
    for value in list:
        if value >= max:
            max = value
        if value <= min:
            min = value
    return (min, max)
print(findMinAndMax([2, 4, 3, 1, 8, 10, 5]))