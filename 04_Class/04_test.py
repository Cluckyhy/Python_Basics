# 用整数0～6依次表示星期日、星期一、星期二、……、星期六，编程实现如下功能：输入一个整数，输出其对应的是星期几。
# 如果输入的整数不在0～6之内，则显示“输入数据错误”。
num = int(input("请输入一个整数："))
if (num < 0 or num > 6):
    print("您输入的数据有误！")
elif (num == 0):
    print("今天星期日")
elif (num == 1):
    print("今天星期一")
elif (num == 2):
    print("今天星期二")
elif (num == 3):
    print("今天星期三")
elif (num == 4):
    print("今天星期四")
elif (num == 5):
    print("今天星期五")
elif (num == 6):
    print("今天星期六")
