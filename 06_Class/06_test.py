# （2）输入任意多个整数，以0作为结束。求这批数中的所有偶数的最大值。
num = int(input("请输入整数(以0作为结束)："))
Max = 1
while num != 0:
    if num % 2 == 0:
        if num > Max:
            Max = num
    num = int(input("请输入整数(以0作为结束)："))
if Max % 2 == 0:
    print("这批数中的所有偶数的最大值为：{}.".format(Max))
else:
    print("您输入的所有数中没有偶数")