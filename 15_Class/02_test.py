# -*- coding = utf-8 -*-
# @Time : 2022/5/31 10:43
# @Author : Cluckyhy
# @File : 02_test.py
# @Software : PyCharm

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import openpyxl

# 创建和访问数据框
# 可以把df数据框 看成一个共享索引的Series对象
datadic = {'apple': [1100, 1050, 1200], 'huawei': [1250, 1300, 1328], 'vivo': [800, 890, 750]}
# df = DataFrame(datadic, index=['一月', '二月', '三月'])
# df = DataFrame(datadic, columns=['一月', '二月', '三月'])
df = DataFrame(datadic, columns=['apple', 'huawei', 'vivo'], index=['一月', '二月', '三月'])
print(df.shape)
print(df)
print()

print("-------------------")
# 输出该df数据框的行索引和列索引
print(df.index)
print(df.columns)
print()

print("--------------------")
# 通过数据列名输出一个Series对象
print(df.apple)
print(df.huawei)
print(df.vivo)
print()
print("--------------------")

# 通过标签索引进行查找数据
print(df.loc['一月'])
print()
print(df.loc['一月':'二月'])
print()
print(df.loc['一月':'二月', 'apple':'huawei'])
print()

print("-----------------------")
# 通过整数索引查找数据
print(df.iloc[2])
print()
print(df.iloc[0:2])
print()
print(df.iloc[0:2, 0:2])
print()

print("-------------------------")
# 取出单个数据
print(df.at['一月', 'apple'])
print(df.iat[0, 0])
print()

# 查询语句
print("------------------------")
print("找出huawei手机价格大于 1300 的数据：")
print(df.query('huawei>1300'))
print()
print("-------------------------")

# 保存文件
df.to_csv('csv/result.csv', encoding='utf-8')
df.to_excel('excel/result.xlsx', sheet_name='sheet1', encoding='utf-8')

df2 = pd.read_excel('excel/fruit.xlsx', index_col=0)
print(df2)

df3 = pd.read_csv('csv/result.csv',index_col=0)
print(df3)
