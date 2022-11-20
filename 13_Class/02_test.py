# 练习创建numpy数组的各种方法
import numpy as np

# 方式1  array()
print("方式1 -- array()")
array_01 = np.array([1, 2, 3, 4, 5])
print("array_01 的默认类型是：", array_01.dtype)
array_01 = np.array([1, 3, 5, 7, 9], dtype=float)
print("指定float数据类型后的 array_01 数组：", array_01)
print("array_01 数组的元素类型为：", array_01.dtype)

# 方式2 arange()
print("\n方式2 -- arange()")
arrar_02 = np.arange(1, 12, 2).reshape(2,3)
print("array_02 数组：")
print(arrar_02)

# 方式3 random.randn()    具有标准正太分布 N(0,1)
print("\n方式3 -- random.randn()")
array_03 = np.random.randn(3,4)
print("array_03 数组：")
print(array_03)

# 方式4 random.randint() 在区间[1,100) 内随机生成5个整数
print("\n方式4 -- random.randint()")
array_04 = np.random.randint(1,100,5)
print("array_04 数组：")
print(array_04)

# 方式5 random.randint() 生成 5X3 数组，值在区间 [1,100) 内
print("\n方式5 -- random.randint() 具有维度")
array_05 = np.random.randint(1,100,(5,4))
print("array_05数组：")
print(array_05)

# 方式6 random.uniform() 生成3X4随机小数数组，值在区间[1,3)
print("\n方式6 -- random.uniform()")
array_06 = np.random.uniform(1,3,(3,4))
print("array_06数组：")
print(array_06)

# 方式7 zeros((3,4)) 全 0 数组
print("\n方式7 -- random.zeros()")
array_07 = np.zeros((3,4))
print("array_07数组：")
print(array_07)

# 方式8 ones((3,4)) 全 1 数组
print("\n方式8 -- random.ones()")
array_08 = np.ones((3,4))
print("array_08数组：")
print(array_08)

# 方式9 单位矩阵
print("\n方式9 -- random.eye()")
array_09 = np.eye(5)
print("array_09数组：")
print(array_09)

# 方式10 全为1.5
print("\n方式10 -- random.full()")
array_10 = np.full((3,4),1.5)
print("array_10数组：")
print(array_10)

# 方式11 重复填充
print("\n方式11 -- random.tile()")
array_11 = np.tile(arrar_02,2)
print("array_11数组：")
print(array_11)

# 方式12 在区间[1,2]内等间距生成10个点，含终值2
print("\n方式12 -- random.linspace()")
array_12 = np.linspace(1,2,4)
print("含终值 array_12数组：")
print(array_12)
# 在区间[1,2]内等间距生成10个点，不含终值2
array_12 = np.linspace(1,5,3,endpoint=False)
print("不含终值 array_12数组：")
print(array_12)
