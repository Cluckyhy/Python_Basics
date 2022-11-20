# -*- coding = utf-8 -*-
# @Time : 2022/6/5 17:17
# @Author : Cluckyhy
# @File : 01_test.py
# @Software : PyCharm
import math
import random

# import numpy as np
# 
# bArray = np.array([[1, 2, 3], [4, 5, 6]])
# print(bArray.shape)
# 
# print(random.randrange(0, 10, 2))
# 
# print(3+5%6*2//8)

from random import *

# Num_list = []
# for i in range(10):
#     print("请输入第", i + 1, "个数：")
#     num = int(input())
#     if num % 2 != 0:
#         Num_list.append(num)
#
# print("所有的奇数有：")
# for item in Num_list:
#     print(item, end=" ")
#
# print("所有奇数中的最大值为：")
# print(max(Num_list))

# sum = 0
# for i in range(2,101):
#     if i%2==0:
#         sum+=i
#     else:
#         sum-=i
# print(sum)

# x =10
# y =4
# print(x/y,x//y)

# s1 = "Thepythonlanguageisa "
# print(s1.split(' '))

# for i in range(1,6):
#     if i/3 == 0:
#         break
#     else:
#         print(i,end=',')

# k =10000
# count = 0
# while k>1:
#     count += 1
#     print(k)
#     k = k/2
# print(count)

# sum = 0
# for i in range(1,11):
#     sum +=i
#     print(sum)
#
# a = 20
# b =a|3
# a&=7
# print(b,end=',')
# print(a)

#

# str = "Hello World"
# print(str[-5:0])
# a = "ac"
# b = "bd"
# c = a+b
# print(c)

# a = []
# for i in range(2, 10):
#     count = 0
#     for x in range(2, i - 1):
#         if i % x == 0:
#             count += 1
#     if count != 0:
#         a.append(i)
# print(a)

# from math import *
# # 定义一个员工信息表
# emp = [
#     ['张三', '财务部', 5000],
#     ['李四', '财务部', 5800],
#     ['王五', '行政部', 5100],
#     ['赵六', '行政部', 5300],
#     ['张华', '技术部', 6200],
#     ['李八', '技术部', 6500],
#     ['张扬', '技术部', 6300],
#     ['陈九', '技术部', 6500]
# ]
#
# sum_sal = 0
# avg_sal = 0
# for item in emp:
#     if "张" in item[0]:
#         sum_sal += item[2]
# avg_sal = sum_sal / len(item)
#
# print("姓张的员工的总工资为：",sum_sal)
# print("姓张的员工的平均工资为：{:.2f}".format(avg_sal))

from math import *

# 提示用户输入一个长度为5的正整数M
num = int(input("请您输入一个长度为5的正整数M："))
if 9999 < num < 100000:
    num_odd = []
    num_ok = []
    for i in range(1, num + 1):
        if i % 2 != 0 and num % i == 0:
            num_odd.append(i)
        if num % i == 0 and sqrt(i) % 1 == 0:
            num_ok.append(i)
    # 从大到小输出M所有的奇数因子
    num_odd = sorted(num_odd, reverse=True)
    print("从大到小输出M所有的奇数因子为：")
    for item in num_odd:
        print(item, end=" ")

    print("\n从小到大输出M所有符合该因子刚好是某个数的平方值：")
    for item in num_ok:
        print(item, end=" ")
else:
    print("请输入一个5位数！")