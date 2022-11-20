# 练习组合和拆分数组
import numpy as np

# 创建一个4X6的二维数组
array_01 = np.arange(24).reshape(4, 6)
# 显示array_01 数组
print("array_01 数组为：")
print(array_01)

# 拆分

# 水平拆分数组
h1, h2 = np.hsplit(array_01, 2)
print("前一半：")
print(h1)
print("后一半：")
print(h2)

# 竖直拆分数组
v1, v2 = np.vsplit(array_01, 2)
print("上一半：")
print(v1)
print("下一半：")
print(v2)

# 组合
array_02 = np.array([11, 22, 33, 44, 55])
array_03 = np.array([99, 88, 77, 66, 55])

# 水平组合
print("\n水平组合：")
print(np.hstack((array_02, array_03)))

# 竖直组合
print("\n竖直组合：")
print(np.vstack((array_02, array_03)))
