# 读取二进制文件（视频，图片）需要用"rb"
# w是写，直接覆盖已有文件内容，a则是追加到后面
# 第三个参数可以传编码，比如encoding="gbk"
# 第四个参数可以传error，以免遇到错误
with open('./test.txt', 'a') as f1:
    f1.write("11111\n2222")
with open('./test.txt', 'r', encoding="gbk", errors="ignore") as f2:
    for line in f2.readlines():
        print(line.strip())