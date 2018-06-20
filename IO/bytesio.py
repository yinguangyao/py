# BytesIO只能用来操作二进制数据
from io import BytesIO
f = BytesIO()
# 这里不是字符串，而是编码过的bytes
f.write("中文".encode("utf-8"))
print(f.getvalue())