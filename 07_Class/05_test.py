# 5、创建列表listfib=[1,1]，要求最后该列表中保存有斐波那契数列：1,1,2,3,5,8,13,21,34,...前50项元素。

listFib = [1, 1]
for i in range(2, 50):
    listFib.append(listFib[i - 2] + listFib[i - 1])
print(listFib)
