# 踩坑：这里isfile和isdir里面要存放完整路径，不然会返回false
# 关键点在于递归
import os
def search_files(path):
    files = [os.path.join(os.path.abspath(path), x) for x in os.listdir(path) if os.path.isfile(os.path.join(os.path.abspath(path), x)) and x.find(".py") > 0]
    dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(os.path.abspath(path), x))]
    print(files)
    for dir in dirs:
        search_files(os.path.join(path, dir))
search_files(os.path.abspath(r'/Users/yinguangyao/Desktop/desktop/project/python'))