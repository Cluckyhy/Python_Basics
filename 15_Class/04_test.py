# -*- coding = utf-8 -*-
# @Time : 2022/5/31 12:08
# @Author : Cluckyhy
# @File : 04_test.py
# @Software : PyCharm

import numpy as np
from pandas import Series, DataFrame

# 构造一个字典数据
dataDic = {'id': [1, 2, 3], 'name': list('ABC'), 'engScore': [89, 65, 99], 'mathScore': [79, 88, 100]}
df = DataFrame(dataDic, index=list(range(1, 4)))
print(df)
print("------------------------")
df.set_index('id', inplace=True)
print(df)

print(df.iloc[:, 1:3].sum())
print(df.iloc[:, 1:3].mean())
print(df.iloc[:, 1:3].count())
print(df.iloc[:, 1:3].max())
print(df.iloc[:, 1:3].min())
# var()求的是样本方差
print(df.iloc[:, 1:3].var())
