# -*- coding = utf-8 -*-
# @Time : 2022/5/31 19:52
# @Author : Cluckyhy
# @File : 07_test.py
# @Software : PyCharm

import pandas as pd
from pandas import Series, DataFrame

df = pd.read_excel('excel/score.xlsx')

# 计算每个同学的平均分[平均分 = (课程1+课程2)/2]
df['平均分'] = (df['math'] + df['english']) / 2
# 使用rank()方法按平均分给出一个全年级的名次排名
df['排名'] = df['平均分'].rank(ascending=False)
print(df)

df2 = df.sort_values(by='排名')
print(df2)

print(df.groupby('班级')['math', 'english'].mean())
print(df.groupby('性别').size())
print(df.groupby('性别')['math', 'english'].mean())
