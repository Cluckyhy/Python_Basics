# 练习数组的基本运算
import numpy as np

# 创建一个一维数组
array_01 = np.arange(1, 6)
print("array_01 数组为：")
print(array_01)

print(array_01 + 5)
print(array_01 - 2)
print(array_01 * 3)
print(array_01 / 2)

# 再创建一个一维数组
array_02 = np.arange(10, 15)
print("\narray_02 的数组为：")
print(array_02)

# 进行两个数组的运算
print("\n两个数组相加为：")
print(array_01 + array_02)

print("\n两个数组相乘为：")
print(array_01 * array_02)

print("\n两个数组相除为：")
print(array_01 / array_02)