# （5）编程求数列1，2，-3，4，5，-6，7，8，-9，10，11，-12，….， 988，-999，1000所有元素之和。
# 定义一个起始数
num = 1
# 定义一个总和变量
Sum = 0
# 利用while循环语句来实现数列所有元素之和
while num <= 1000:
    if num % 3 == 0:
        num = -num
    Sum += num
    num = abs(num) + 1
print("数列1，2，-3，4，5，-6，7，8，-9，10，11，-12，….， 988，-999，1000所有元素之和：")
print(Sum)