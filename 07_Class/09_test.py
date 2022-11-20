# 3. 编程实现“小学四则运算测试机”系统。 系统随机产生[ 1,10 ]之间的两个操作数，随机产生一个运算符 ( +, -, *, / )，
# 把操作数和运算符作为一个算式题目显示给用户看，用户输入算式的运算结果。程序判断是否正确，并给出提示如“您答对了”或“您算错了”。
# 不管是否答对，同一道题，只答一次。
# 让用户不停地答题，直到他输入’10000’，退出答题。
# 例如：系统显示题目 3+6，用户输入9，系统显示“您答对了”。
# 系统显示题目 3*6，用户输入9，系统显示“您算错了”。

from random import *

num1 = randint(1, 10)
num2 = randint(1, 10)

operatorList = ['+', '-', '*', '/']
n = randint(0, 3)
str = str(num1) + operatorList[n] + str(num2)
print(str)
while True:
    print("请用户答题--->", end="")
    result = eval(input("用户答案为："))
    if result != eval(str):
        if result == 10000:
            print("已经退出程序！")
            break
        print("很遗憾，你打错了！")
    else:
        print("恭喜你，答对了！")
        break

