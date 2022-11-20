# 索引访问 numpy 数组的各种方法
import numpy as np

# 一维数组的访问练习
array_01 = np.arange(10, 20)
print("array_01 数组为：", array_01)
print("数组第一个元素为：", array_01[0])
print("数组最后一个元素为：", array_01[-1])
print("数组下标为2到下标为5的元素内容为：", array_01[2:5])
print("数组下标为列表中的数组元素为：", array_01[[1, 4, 5, 8]])

# 二维数组的访问练习
array_02 = np.arange(24).reshape(4, 6)
print("\narray_02 数组为：")
print(array_02)
print("第一行数据为：", array_02[0])
print("第二行的第三个数据为：", array_02[1, 2])
print("前两行数据为：")
print(array_02[:2])
print("第二行到最后一行的第2个元素到第三个元素")
print(array_02[1:, 1:3])
print("得到所有行的从第一个元素开始步长为2的元素：")
print(array_02[:, ::2])

# array_03 是 array_02[1] 的视图
array_03 = array_02[1]
print("\narray_03 为 array_02[1] 的视图：")
print(array_03)
# 修改视图 array_03的数据
array_03[0] = 100
# 查看array_02的数据
print(array_02)  # 发现，修改视图也会把源数组修改

# array_04 是 array_02[2] 的复制
array_04 = array_02[2].copy()
print("\narray_04 为 array_02[2] 的复制为：")
print(array_04)
# 修改 array_04 的 某个元素的值后
array_04[1] = 666
print("\n复制的数组发生变化：")
print(array_04)
print("\n而源数组不会发生变化：")
print(array_02)
