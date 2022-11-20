# 2.基本统计值的计算。平均值、标准差、中位数是进行数据分析和统计的有用指标，
# 一组数据表示为S=s_0,s_1,⋯,s_(n-1)，其算术平均值、标准差分别计算如下：
# 而中位数是指S中的所有数按照从小到大（或者从大到小）顺序排列后，处于最中间位置的数据值。如果n是奇数，
# 则序列S的最中间位置是一个数据，可以表示为s_(n//2)，如果n是偶数，序列S不存在一个最中间位置，
# 则中位数表示为最中间两个位置数据的平均值，即(s_(n//2-1)+s_(n//2))/2。
# 请使用IPO（输入、处理、输出）的程序编写方法，实现由用户从控制台输入10个数据，
# 存放到列表中，完成算术平均值、标准差和中位数的计算，并输出。
# （注意：此处需要根据上面三个指标的计算公式自行实现计算，不能调用现成的均值、标准差、中位数相关函数）

from math import floor
statsList = eval(input("请一次性输入10个数据(两端要加中括号，两个数之间用逗号隔开)："))
print("列表为：", statsList)
sumNum = 0
count = 0
for item in statsList:
    count += 1
    sumNum += item
averAge = sumNum / count
print("总和为：", sumNum)
print("平均值为：", averAge)

sumNum2 = 0
for item in statsList:
    sumNum2 += (item - averAge) ** 2
sd = (sumNum2 / (count - 1)) ** 0.5
print("标准差的值为：", sd)
statsList.sort(reverse=True)
lenList = len(statsList)
sumMiddle = 0
if lenList % 2 == 0:
    sumMiddle = (statsList[floor(lenList / 2 - 1)] + statsList[floor(lenList / 2)]) / 2
else:
    sumMiddle = statsList[floor(lenList/2)]
print("中位数为：", sumMiddle)
