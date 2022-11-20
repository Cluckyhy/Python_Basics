# -*- coding = utf-8 -*-
# @Time : 2022/5/31 12:55
# @Author : Cluckyhy
# @File : 06_test.py
# @Software : PyCharm

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dataDic = {'apple': [1100, 1050, 1200], 'huawei': [1250, 1300, 1328], 'oppo': [800, 850, 750]}
df = DataFrame(dataDic, index=['一月', '二月', '三月'])
print(df)
print("-------------------------")
# 删除行 一月，返回一个新的df对象，不直接改变df
df2 = df.drop('一月')
print(df)
print(df2)
print("-------------------------")
# 删除 oppo 列，直接改变df
df3 = df.pop('oppo')
print(df)
# 输出删除的那一列数据
print(df3)
print("-------------------------")

# 剔除 二月，新增 四月
df = df.reindex(["一月", "三月", "四月"])
print(df)
print("--------------------------")

# inplace 参数为True：是指不创建新对象，而是直接在原对象进行修改
# inplace 参数为False：是指对数据进行修改，创建并返回新的对象承载其修改的结果
# 该参数的默认值为 False
df.reset_index(inplace=True)
print(df)
print("-------------------------")

# 将apple列设为索引列
df4 = df.set_index('apple', inplace=False)
print(df4)
print("---------------------------")

# 追加数据
# df = df.append({'index': '五月', 'apple': 7888, 'huawei': 9999}, ignore_index=True)
# # pd.concat({'index': '五月', 'apple': 7888, 'huawei': 9999}, ignore_index=True)
# print(df)

df5 = DataFrame({'product': ['A', 'B', 'C', 'A'], 'color': ['r', 'g', 'r', 'r']})
print(df5)
print("----------------------------")
# 输出重复的行，True表示重复与前面的有重复
print(df5.duplicated())
print("----------------------------")
# 删除重复的行数
print(df5.drop_duplicates())
print("----------------------------")

df6 = DataFrame({'id': list('axc'), 'quantity': [300, 202, 550], 'ptype': list('BCB')})
df6.set_index('id', inplace=True)
print(df6)
print(df6.sort_index())
print(df6.sort_values('quantity'))
print(df6.sort_values(by='quantity'))
print("-------------------------------")

# 练习构造两个数据框，含有共同的列，练习merge，append,left,right两个合并
df7 = DataFrame({'color': ['r', 'b', 'w', 'w'], 'c1': range(4)})
df8 = DataFrame({'color': ['b', 'w', 'b'], 'c2': range(2, 5)})
df9 = pd.merge(df7, df8)
print(df9)

# 构造区间[0,100]内的80个年龄随机整数，按区间[0,10,18,35,50,70,100] 做 pd.cut()分段统计
ar = np.random.randint(0, 101, 80)
print(ar)
bins = [0, 10, 18, 35, 50, 70, 100]
ar_cat = pd.cut(ar, bins=bins)
print(ar_cat)
# 统计每个区间的人数
print(pd.value_counts(ar_cat))
