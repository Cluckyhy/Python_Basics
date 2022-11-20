# 从键盘上输入球的半径，计算输出球的表面积和体积，要求输入和输出的数字结果之前都具有一定的文字提示。
from math import *

# 键盘输入球的半径
r = eval(input("请输入球的半径"))
# 球的表面积
Area = 4 * pi * r ** 2
print("球的表面积为：", Area)

# 球的体积
Volume = (4 * pi * r ** 3) / 3
print("球的体积为：", Volume)
