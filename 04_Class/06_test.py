# 输入任意三个整数，将它们按照从大到小的顺序输出。
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数"))
num3 = int(input("请输入第三个整数"))
if (num1 < num2):
    if (num2 < num3):
        Max = num3
        Middle = num2
        Min = num1
    elif(num1>num3):
        Max = num2
        Middle = num1
        Min = num3
    else:
        Max = num2
        Middle = num3
        Min = num1
    print("三个整数从大到小的顺序为：", Max, Middle, Min)
else:
    if (num1 < num3):
        Max = num3
        Middle = num1;
        Min = num2
    elif (num2 > num3):
        Max = num1
        Middle = num2
        Min = num3
    else:
        Max = num1
        Middle = num3
        Min = num2
    print("三个整数从大到小的顺序为：", Max, Middle, Min)
