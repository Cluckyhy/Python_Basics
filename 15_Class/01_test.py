# -*- coding = utf-8 -*-
# @Time : 2022/5/31 10:02
# @Author : Cluckyhy
# @File : 01_test.py
# @Software : PyCharm

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# 打印显示pandas的版本
print("当前的pandas版本为：", pd.__version__)
# 创建一个Series对象
s = Series(np.arange(6), index=list('abcdef'))
print("当前Series对象为：")
print(s)

print("Series的索引值为：", s.index)
print("Series的数据为：", s.values)

# 通过标签索引访问数据
print("通过标签索引访问数据")
print("Series索引为a 的数据为：", s['a'])
print("Series索引为b 的数据为：", s['b'])
print("Series索引为c 的数据为：", s['c'])

# 通过整数索引访问数据
print("\n通过整数索引访问数据")
print("Series索引为3 的数据为：", s[3])
print("Series索引为4 的数据为：", s[4])
print("Series索引为5 的数据为：", s[5])

# 赋值修改
s['c', 'e'] = 3
print(s)

# 统计函数
print("Series对象的总和为：", s.sum())
print("Series对象的平均值为：", s.mean())
print("Series对象的中位数为：", s.median())

# 统计数据的频次
print("Series对象的数据频次为：")
# 默认是有排序的
print(s.value_counts())
print(s.value_counts(sort=False))

# 返回不重复的数据列
print("返回不重复的数据列")
print(s.unique())

# 显示数据的头3个数据
print("显示数据的头3个数据")
print(s.head(3))

# 显示数据的最后3个数据
print("显示数据的最后3个数据")
print(s.tail(3))

# 定义另外一个Series对象
s2 = Series(np.arange(12, 30, 3), index=list('abcdef'))
# s 和 s2 进行运算
print("s + s2 的结果为：")
print(s + s2)

print("s * s2 的结果为：")
print(s * s2)