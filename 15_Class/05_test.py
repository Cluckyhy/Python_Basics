# -*- coding = utf-8 -*-
# @Time : 2022/5/31 12:30
# @Author : Cluckyhy
# @File : 05_test.py
# @Software : PyCharm

import pandas as pd
from pandas import Series, DataFrame

df = pd.read_csv('csv/fee.csv', encoding='utf-8')
print(df)
df.to_csv('csv/fee2.csv', encoding='utf-8', index=False)

df.to_excel('excel/fee2.xlsx', index=False)
df2 = pd.read_excel('excel/fee2.xlsx')
print(df2)
