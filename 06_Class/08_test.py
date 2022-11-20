# （4）输入任意一个三位数（注意：必须是三位数）的整数，判断其是否为素数。
num = int(input("请输入任意三位数的整数："))
while num < 100 or num > 999:
    print("你输入的数不是三位数，请重新输入！")
    num = int(input("请输入任意三位数的整数："))
for i in range(2, num):
    if num % i == 0:
        print("{}不是素数".format(num))
        break
# 利用循环中的else语句
else:
    print("{}是素数".format(num))
