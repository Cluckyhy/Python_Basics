# 2.编写程序，从键盘上输入若干个整数，以输入数字0为结束。求出这些整数中所有奇数之和、偶数之和及所有数的平均值。
num = int(input("请输入整数(以输入数字0为结束)："))
# 奇数总和变量
sum_odd = 0
# 偶数总和变量
sum_even = 0
# 所有数的总和
Sum = 0
# 计数器
count = 0
while num != 0:
    count = count + 1
    Sum += num
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
    num = int(input("请输入整数(以输入数字0为结束)："))
Average = Sum / count
print("这些整数中所有奇数之和为：{},偶数之和{},所有数的平均数为：{}".format(sum_odd, sum_even, Average))
