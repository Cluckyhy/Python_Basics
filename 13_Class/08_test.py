# 练习 读写文件
import numpy as np

# 创建一个二维数组
array_01 = np.arange(12).reshape(3, 4)
print("array_01 数组为：")
print(array_01)

# 存为文本文件
np.savetxt("data.txt", array_01, delimiter=',', fmt="%d")

# 读取文本文件
array_02 = np.loadtxt("data.txt", delimiter=',', dtype=int)

print("array_02 数组为：")
print(array_02)

print(array_02 == array_01)
