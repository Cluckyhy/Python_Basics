# 3、设有列表listodd=[1,3,5,7,9] 和列表 listeven=[2,4,6,8,10]。
# 编写程序，将两个列表合并成一个新列表，要求新的列表中的元素按从大到小的顺序排列。
# 不能改变原有列表listodd和listeven的值。

listOdd = [1, 3, 5, 7, 9]
listEven = [2, 4, 6, 8, 10]
oldList = listOdd + listEven
print("排序前的列表为：")
print(oldList)
newList = sorted(oldList,reverse=True)
print("排序后的列表为：")
print(newList)
print("查看listOdd")
print(listOdd)
print("查看listEven")
print(listEven)
