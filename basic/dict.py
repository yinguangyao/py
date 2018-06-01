# dict插入和查询速度非常快，但是占用内存更多
# list则相反，所以dict是用空间换取时间的做法
# dict访问不存在的属性会报错，可以用get来访问，类似lodash的get
# pop方法可以删除某个属性
# dict的key值一定是不可变数据，所以不能是list
# 但是tuple反而可以
d = {"name": "ygy", "age": 22}
print(d["name"])
print(d.get("sex"))
d.pop("name")
del d["age"] # 删除
print(d)
arr = (1, 2, 3)
d[arr] = 10
print(d[arr])