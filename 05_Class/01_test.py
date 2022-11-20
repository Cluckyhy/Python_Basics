# （1）编程输出1000以内所有能同时被3和4整除的数，以及这些数的个数、这些数的和。
# 定义初始值
num = 1
# 定义元素和变量
Sum = 0
# 定义个数变量
count = 0
# 利用while循环来求解
print("1000以内的所有同时能被3和4整除的数有：", end=" ")
while num <= 1000:
    if num % 3 == 0 and num % 4 == 0:
        if count % 10 == 0:
            print("\n")
        count = count + 1
        print(num, end=" ")
        Sum += num
    num = num + 1
print("\n这些数的个数为：")
print(count)
print("这些数的和为：")
print(Sum)
