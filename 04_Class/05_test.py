# 编程求一元二次方程Ax2+Bx+C=0的解。要求区分输入的系数A、B、C的各种可能取值，求解相应的方程。
from math import *

A = int(input("请输入x平方的系数："))
B = int(input("请输入x的系数："))
C = int(input("请输入常熟C："))
if (A == 0):
    if (B == 0):
        if(C == 0):
            print("此方程的解可以是任意的")
        else:
            print("此方程无解！")
    else:
        result = (-C) / B
        print("此方程只有一个解，且解为：", result)
else:
    num1 = B ** 2 - 4 * A * C
    if (num1 > 0):
        num2 = sqrt(num1)
    else:
        num2 = 0
    if (num1 == 0):
        result = ((-B) + num2) / 2 * A
        print("此方程的解为：", result)
    elif (num1 > 0):
        result1 = ((-B) + num2) / 2 * A
        result2 = ((-B) - num2) / 2 * A
        print("此方程的解为：", result1, "和", result2)
    else:
        print("此方程无解！")
