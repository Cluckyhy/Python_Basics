# 4.在 [1, 100] 之间产生两个随机整数a，b，求a，b的最大公约数和最小公倍数。
from random import *

# 随机产生两个1到100之间的整数
num1 = randint(1, 100)
num2 = randint(1, 100)
if num1 > num2:
    Max = num1
    Min = num2
else:
    Max = num2
    Min = num1
# print("较大数：", Max)
# print("较小数：", Min)
# 求num1,num2中的最小公约数
# min_divisor
for i in range(Min, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print("{}和{}的最大公约数为：{}".format(num1, num2, i))
        max_multiple = num1 * num2 / i
        print("{}和{}的最小公倍数为：{}".format(num1, num2, max_multiple))
        break
