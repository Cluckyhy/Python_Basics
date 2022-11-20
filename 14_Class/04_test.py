# -*- coding = utf-8 -*-
# @Time : 2022/5/24 10:23
# @Author : Cluckyhy
# @File : 04_test.py
# @Software : PyCharm
import numpy as np
import matplotlib.pyplot as plt

# 利用matplotlib库中的pyplot模块，绘制x在[-10,10]取值区间上的函数 f(x)=x^3+2x^2+3x+4
# f(x)一阶导数和二阶导数的图形要求
# （1）绘制三个子图，分别放置上述三个图形
# （2）第一个子图区域，标题为Polynomial，使用红色实线绘制
# （3）第二个子图区域，标题为First Derivative，使用蓝色虚线绘制
# （4）第三个子图区域，标题为Second Derivative，使用绿色实心圆点绘制
plt.rcParams['font.family'] = 'Kaiti'   # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 设置负号显示正常
x = np.arange(-10,11)   # x在[-10,10]取值区间
# 先通过系数数组A生成多项式
A = np.array([1,2,3,4])
f = np.poly1d(A)
y = np.polyval(f,x)
# 绘制第一个子图区域，标题为Polynomial，使用红色实线绘制
plt.subplot(3,1,1)
plt.title("Polynomial")
plt.ylim(-1000,1500)
plt.plot(x,y,'r-')

# 求出函数f(x)=x^3+2x^2+3x+4的一阶导数
f1 = np.polyder(f)
y1 = np.polyval(f1,x)
# 第二个子图区域，标题为First Derivative，使用蓝色虚线绘制
plt.subplot(3,1,2)
plt.subplots_adjust(hspace=2)
plt.title("First Derivative")
plt.ylim(0,500)
plt.plot(x,y1,'b:')

# 求出函数f(x)=x^3+2x^2+3x+4的二阶导数
f2 = np.polyder(f,2)
y2 = np.polyval(f2,x)
# 第三个子图区域，标题为Second Derivative，使用绿色实心圆点绘制
plt.subplot(3,1,3)
plt.subplots_adjust(hspace=2)
plt.title("Second Derivative")
plt.ylim(-100,100)
plt.plot(x,y2,'go')

# 显示图形
plt.show()