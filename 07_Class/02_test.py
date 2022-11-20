# 2、编写程序，生成一个包含20个两位数的随机整数的列表，将其前十个元素升序排列，后十个元素降序排列。
from random import randint

numList = []
for i in range(0, 20):
    numList.append(randint(10, 100))
print("原始列表为：\t\t", numList)
List1 = numList[0:10]
print("前10个元素为：\t", List1)
List2 = numList[10:20]
print("后10个元素为：\t", List2)
List1.sort()
List2.sort(reverse=True)
numList = List1 + List2
print("前10个元素升序，后10个元素降序的结果为：")
print(numList)
