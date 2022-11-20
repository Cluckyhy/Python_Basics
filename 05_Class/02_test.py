# （2）编程求数列1，1，2，3，5，8，13，21，34， …… 中第一个超过300的数，并注明是第几个数。
# 首先定义两个头元素
num1, num2 = 1, 1
# 定义一个求前两个数之和的变量
Sum = 0
# 定义一个变量来计数
count = 2
# 利用循环来实现
while Sum < 300:
    Sum = num1 + num2
    num1 = num2
    num2 = Sum
    count = count + 1
print("数列中第一个超过300的数为：", Sum)
print("这个数在数列中是第：", count, "个数")
