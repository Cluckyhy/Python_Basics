# -*- coding = utf-8 -*-
# @Time : 2022/5/31 20:25
# @Author : Cluckyhy
# @File : 08_test.py
# @Software : PyCharm

import pandas as pd
from pandas import DataFrame

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180)  # 设置打印宽度(重要)

# 1、利用 pandas 库中的 read_csv()函数读取 '2018世界杯球队数据.csv' 中的数据，并存入一个DataFrame对象中
df = pd.read_csv('csv/2018世界杯球队数据.csv', encoding='GBK', index_col=0)

# 2、输出净胜球(进球数减去失球数)大于0的球队
print("净胜球((进球数减去失球数)大于0的球队有：")
marginBall = df.where((df['进球'] - df['失球']) > 0)
marginBall = marginBall.dropna()
# print(marginBall.iloc[:, :4])
print(marginBall[['球队', '进球', '失球']])

print("\n=========================================================\n")
# 3、输出被罚红牌的球队
print("被罚红牌的球队有：")
print(df.query('红牌>0')[['球队', '红牌']])

print("\n=========================================================\n")
# 4、输出进球成功率(进球数/射门数)超过10%的球队及其进球数和射门数
print("进球成功率(进球数/射门数)超过10%的球队及其进球数和射门数")
goalRate = df.where((df['进球'] / df['射门']) > 0.1)
goalRate = goalRate.dropna()
print(goalRate[['球队', '进球', '射门']])

print("\n=========================================================\n")
# 5、输出进球数超过平均数且被罚黄牌少于5张的球队及其进球数和黄牌数
# 首先得到进球平均数
avgBall = df['进球'].mean()
print("进球平均数为：", avgBall)
UpAvg = df.where(df['进球'] > avgBall)
UpFine = UpAvg.where(UpAvg['黄牌'] < 5)
UpFine = UpFine.dropna()
print("进球数超过平均数且被罚黄牌少于5张的球队及其进球数和黄牌数如下：")
print(UpFine[['球队', '进球', '黄牌']])

print("\n=========================================================\n")
# 6、按照进球数降序输出所有球队及进球信息
SortBall = df.sort_values(by='进球', ascending=False)
print("按进球数降序输出所有球队及进球信息为：")
print(SortBall.iloc[:, :11])

print("\n=========================================================\n")
# 7、按照所属区进行分组，按升序统计输出每个区的进球数
tmp = df.groupby(by='所属洲')['进球'].sum()
print("每个区的进球数为(升序)：")
tmp = tmp.sort_values()
print(tmp)
