# 数组统计函数的练习
import numpy as np

# 设置一个随机种子
np.random.seed(5)

# 创建一个用随机数生成的一维数组
array_01 = np.random.randint(1, 13, (3, 4))
print("array_01 数组为：")
print(array_01)

# 计算数组的均值
print("\n数组的均值为：")
print(array_01.mean())
print(np.mean(array_01))

# 计算轴为0的均值
print("\n数组轴为0的均值为：")
print(array_01.mean(axis=0))
print(np.mean(array_01, axis=0))

# 计算轴为1的均值
print("\n数组轴为1的均值为：")
print(array_01.mean(axis=1))
print(np.mean(array_01, axis=1))

# 计算array_01 的方差
print("\n数组的方差为：")
print(array_01.var())
print(np.var(array_01))

# 计算array_01 的标准差
print("\n数组的标准差为：")
print(array_01.std())
print(np.std(array_01))

# 计算array_01 的sin值
print("\n数组的sin值为：")
print(np.sin(array_01))

# 将高维数组转换为一维数组
print("\n将高维数组转换为一维数组后为：")
array_02 = array_01.flatten()
print(array_02)

# 按指定轴返回数组元素的累计的和
print("\n按指定0轴返回数组元素的累计的和：")
print(array_01.cumsum(axis=0))
print(np.cumsum(array_01, axis=0))

print("\n按指定1轴返回数组元素的累计的和：")
print(array_01.cumsum(axis=1))
print(np.cumsum(array_01, axis=1))

# 按指定0轴返回数组中最小元素的对应索引构成的数组
print("\n按指定0轴返回数组中最小元素的对应索引构成的数组：")
print(array_01.argmin(axis=0))
print(np.argmin(array_01, axis=0))

print("\n按指定1轴返回数组中最小元素的对应索引构成的数组：")
print(array_01.argmin(axis=1))
print(np.argmin(array_01, axis=1))

# 按指定轴返回数组元素的最大值
print("\n按指定0轴返回数组中最大值元素：")
print(array_01.max(axis=0))
print(np.max(array_01, axis=0))

print("\n按指定1轴返回数组中最大值元素：")
print(array_01.max(axis=1))
print(np.max(array_01, axis=1))
