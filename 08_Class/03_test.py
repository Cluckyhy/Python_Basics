# 创建一个字典
dic_user = {"John": "123", "Marry": "111", "Tommy": "123456"}

# 提示用户输入用户名和密码
while True:
    account = input("请用户输入用户名：")
    if account not in dic_user.keys():
        print("用户名不正确！请您重新输入：")
    else:
        break
while True:
    password = input("请用户输入密码：")
    if password not in dic_user.values():
        print("密码不正确！请您重新输入：")
    else:
        break
print("恭喜你，登录成功！")
