# -*- coding = utf-8 -*-
# @Time : 2022/5/31 12:01
# @Author : Cluckyhy
# @File : 03_test.py
# @Software : PyCharm

from pandas import Series
import numpy as np

# 构造一个含有NAN值的Series，练习isnall(),notnall(),dropna(),fillna()等函数
s = Series(np.array([2, 3, np.nan, np.nan, None]))
print("数据为null的值为true")
print(s.isnull())
print("数据不为null的值为true")
print(s.notnull())
print("删除数据为NAN的值")
print(s.dropna())
print("把数据为null的值全部填充为指定的值")
print(s.fillna(100))
