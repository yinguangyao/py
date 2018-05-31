# 条件判断语句中，如果通过了第一个条件，就不会执行后面的条件了
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# 切记输入的是个字符串，在这里一定要用int转为数字
s = int(input("请输入数字"))
if s < 100:
    print("小于100")
else:
    print("大于等于100")
