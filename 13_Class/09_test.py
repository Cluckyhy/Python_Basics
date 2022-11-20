# 练习
import numpy as np
from collections import Counter

# 1、先创建一个 9 X 9 的全1二维数组，再将二维数组四条边上的数据都修改为0

array_01 = np.ones((9, 9), dtype=int)
array_01[0::8, :] = 0
array_01[:, 0::8] = 0
print("array_01 数组为；")
print(array_01)

# 2、在区间[1,6]内生成1000个随机数，统计每个整数出现的次数
# 统计方法一：
array_02 = np.random.randint(1, 7, 1000)
print(Counter(array_02))
# 统计方法二：
print(np.unique(array_02))
for i in np.unique(array_02):
    print(i, np.sum(array_02 == i), end="\t")
print()

# 练习数组的插入(insert) 和 删除(delete)
array_03 = np.arange(4)
print(array_03)
array_03 = np.append(array_03, 10)
print(array_03)
array_03 = np.insert(array_03, 2, 5)
print(array_03)
array_03 = np.delete(array_03, [2, 3])
print(array_03)

# 生成 2X3 和 3X3 两个数组，利用 np.dot()计算数组的矩阵乘法
# 计算方式是用 array_04的每一行去乘array_05的每一列得到的和，最后的结果的行数和array_04的行数一样
array_04 = np.arange(6).reshape(2, 3)
print("\narray_04 :")
print(array_04)
array_05 = np.arange(6).reshape(3, 2)
print("\narray_05 :")
print(array_05)
print("\n矩阵乘法的结果为：")
print(np.dot(array_04, array_05))
print()

# 模拟生成50名同学的单科成绩，符合正太分布 N(70,100)完成排序，求最大值，最小值，均值
array_06 = np.random.normal(loc=70, scale=10, size=50)
print(array_06.max())
print(array_06.min())
print(array_06.mean())

print()
print()

# 利用 numpy 中的多项式处理函数，编程计算 f(x)=x5+2x3+1 在 x = 2 和 x = 5时的值，并输出f(x)的一阶导数和二阶导数
# 利用系数数组生成一个多项式
A = np.array([1, 0, 2, 0, 0, 1])
f = np.poly1d(A)

# 输出多项式
print("多项式为：")
print(f)

# 输出f(x) 在 x = 2 和 x = 5 处的值
print("多项式在 x = 2处的值为：", np.polyval(f, 2))
print("多项式在 x = 5处的值为：", np.polyval(f, 5))

# 求出f(x)的一阶导数
f1 = np.polyder(f)
print("f(x)的一阶导数为：")
print(f1)

# 求出f(x)的二阶导数
f2 = np.polyder(f, 2)
print("f(x)的二阶导数为：")
print(f2)
