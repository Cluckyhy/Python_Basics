from math import *

x = float(input("请输入一个实数x："))
if (x <= 0):
    y = 100 - x ** 2
elif (x <= 20):
    y = sqrt(x + 5)
else:
    y = x - 20
print("y的值为：", y)
