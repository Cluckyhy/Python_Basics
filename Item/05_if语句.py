# 单分支语句
a = int(input("请输入整数a："))
b = int(input("请输入整数b："))
print("输入值 a = {},b = {}".format(a, b))
if a < b:
    a, b = b, a
print("比较后的值 a = {},b = {}".format(a, b))

# 双分支语句
s = input("请输入字符串：")
if s == s[::-1]:
    print(s + "为回文串")
else:
    print(s + "不是回文串")
