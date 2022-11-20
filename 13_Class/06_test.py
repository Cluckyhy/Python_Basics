# 排序练习
import numpy as np

# 设置随机数的种子
np.random.seed(3)

# 创建一个利用随机数生成的一维数组
array_01 = np.random.randint(1, 20, size=10)

# 显示array_01数组
print("array_01 数组：", array_01)

# 将array_01 数组 复制到 array_02 中
array_02 = array_01.copy()

# 将array_02 数组进行排序
array_02.sort()

# 显示array_02 数组
print(array_02)
print(array_01)

array_03 = np.sort(array_01)  # 返回新的有序数组，不该变 array_01数组
print("array_03 数组：", array_03)
print(array_01)

print(array_02[np.argsort(-array_02)])

# np.argsort() 返回按顺序排列时各位上取值对应的索引号
# array_01 数组： [11  4  9  1 11 12 10 11  7  1]
# 排序后的数组为：[ 1  1  4  7  9 10 11 11 11 12]
# 然后，argsort() 后，返回的数组中是值为，对应的数在 array_01 的索引值
# 1对应在array_01的索引为3和9，4对应的索引为1.。。
# 所以有  [3 9 1 8 2 6 0 4 7 5]    最后一个是5，在array_01数组中 5对应的数为12，12是最大的
print(np.argsort(array_01))
