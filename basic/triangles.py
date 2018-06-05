# 杨辉三角
# 由于对python真的不是很熟悉，这里的写法真的是用JS的思维写的

import copy

def triangles():
    n, list1, list2 = 1, [1], [1]
    while n <= 10:
        list2 = [0 for x in range(n)]
        for i in range(n):
            if i == 0:
                list2[i] = list1[i]
                continue;
            if i == (n-1):
                list2[i] = list1[n-2]
                continue;
            list2[i] = list1[i-1] + list1[i]
        list1 = copy.deepcopy(list2)
        n = n + 1
        print(list2)
triangles()
