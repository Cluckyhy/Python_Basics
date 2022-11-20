# 输入一个两位数的整数，交换个位数和十位数的位置，显示处理后的数字。
num1 = int(input("请输入两位数的整数："))
# 求出两位数的个位数
geNum = num1 % 10
# 求出两位数的十位数
shiNum = num1 // 10
print("处理后的数字为："+str(geNum) + str(shiNum))
