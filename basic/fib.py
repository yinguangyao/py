# 斐波拉契数列
def fib(num):
    if(num == 1):
        print(1);
        return
    sum, x, y = 1, 1, 0
    while(sum < num):
        print(sum)
        sum = x + y
        y, x = x, sum
fib(10)
