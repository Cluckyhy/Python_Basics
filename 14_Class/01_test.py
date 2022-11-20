# -*- coding = utf-8 -*-
# @Time : 2022/5/24 9:17
# @Author : Cluckyhy
# @File : 01_test.py
# @Software : PyCharm
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Kaiti'  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 设置负号显示正常

# 利用[2,3,5,10,8]列表数据绘制折线图、柱形图、饼图
data = [2, 3, 5, 10, 8]
labels = list('abcde')
plt.figure()    # 新建折线图形
plt.plot(["a", "b", "c", "d", "e"], data, 'b-')
plt.figure()    # 新建折线图形
x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y,"r")
plt.title("我是图标题")
plt.xlabel("我是x轴标签")
plt.ylabel("我是y轴标签")
plt.text(np.pi,0.6,"我是图文字")
plt.legend(labels = ["我是图例"])
plt.ylim(-2,2)
plt.figure()    # 新建柱状图形
plt.bar(labels,data)
plt.figure()    # 新建饼图
Explode = (0,0.1,0,0.1,0)   # 设置饼块分离
plt.pie(data,explode = Explode,labels = labels,autopct='%1.2f%%')
plt.show()
