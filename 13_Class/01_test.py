# 导入 numpy 第三方库
import numpy as np

# 显示 numpy 版本，注意前后都是下划线
print("当前 numpy 的版本是：", np.__version__)

# 创建二维数组
array_01 = np.arange(15).reshape(3, 5)
print("二维数组如下：")
print(array_01)

# 显示 array_01 的数据类型 numpy.ndarray
print("array_01 数组的数据类型是：", type(array_01))

# 显示 array_01 的形状
print("array_01 数组形状为：", array_01.shape)

# 显示 array_01 的维度
print("array_01 数组维度为：", array_01.ndim)

# 显示 array_01 的元素占用的字节数
print("array_01 数组元素占用字节数为：", array_01.itemsize)

# 显示 array_01 的数组元素个数
print("array_01 数组元素的个数为：", array_01.size)

# 显示数组元素的类型
print("array_01 数组元素的类型为：", array_01.dtype)
