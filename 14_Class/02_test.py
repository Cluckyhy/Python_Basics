# -*- coding = utf-8 -*-
# @Time : 2022/5/24 10:13
# @Author : Cluckyhy
# @File : 02_test.py
# @Software : PyCharm
import numpy as np
import matplotlib.pyplot as plt

# 生成1000个 N(1,10)正太分布的随机小数，绘制箱线图
# N(1,10)则 scale = 10**(1/2)
data = np.random.normal(1,10**(1/2),1000)
plt.boxplot(data)
print('方差',data.var())
plt.show()