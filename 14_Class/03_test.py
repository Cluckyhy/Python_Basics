# -*- coding = utf-8 -*-
# @Time : 2022/5/24 10:16
# @Author : Cluckyhy
# @File : 03_test.py
# @Software : PyCharm
import numpy as np
import matplotlib.pyplot as plt

data = np.arange(1,100)
plt.subplot(2,2,1)
plt.plot(data,data)
plt.subplot(2,2,2)
plt.plot(data,-data)
plt.subplot(2,2,3)
plt.plot(data,data**2)
plt.subplot(2,2,4)
plt.plot(data,np.log(data))
plt.show()