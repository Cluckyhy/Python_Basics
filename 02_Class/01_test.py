"""
（1）5+ (2+3)2
（2）2a(b+5)        #设定a=2, b=3
（3）(-b+√(b^2-4ac))/2a     #设定a=1, b=-6,c=5
（4）√(π^2+3)
（5）ln(2π√(13+e))
（6）tan^(-1)  log_3(π+1)
"""

from math import *

# 第一个表达式
# result = 5 + (2 + 3) * (2 + 3)
# print(result)
#
# 第二个表达式
# a = eval(input("请输入a的值："))
# b = eval(input("请输入b的值："))
# result = 2 * a * (b + 5)
# print(result)
#
# 第三个表达式
# a = eval(input("请输入a的值："))
# b = eval(input("请输入b的值："))
# c = eval(input("请输入c的值："))
# result = (-b + (sqrt((b ** 2) - 4 * a * c))) / (2 * a)
# print(result)

# 第四个表达式
# result = sqrt(pi**2+3)
# print(result)

# 第五个表达式
# result = log(2 * pi * sqrt(13 + e), e)
# print(result)

# 第六个表达式
result = tan((log(pi + 1, 3)) ** -1)
print(result)
