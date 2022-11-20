# （1）输入任意两个正整数，输出它们的所有公约数，并求最大公约数。
while True:
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数："))
    if num1 > 0 and num2 > 0:
        break
    else:
        print("你输入的数有误！请重新输入")
if num1 < num2:
    Min = num1
else:
    Min = num2
print("{}和{}的所有公约数为：".format(num1, num2))
for i in range(1, Min+1):
    if num1 % i == 0 and num2 % i == 0:
        print(i, end=" ")
for i in range(Min, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print("\n{}和{}的最大公约数为：{}".format(num1, num2, i))
        break
