# （3）输入正数n，求n以内能被3整除的最大整数。
num = int(input("请输入一个正数："))
for i in range(num, 0, -1):
    if i % 3 == 0:
        print("{}以内能被3整除的最大整数为：{}".format(num, i))
        break
