# 1. 定义一个含有两个参数的重复打印函数，第一个参数指定要打印的字符串，
# 第二个参数指定要重复打印的次数，在主程序中调用该函数，打印10遍你的姓名。

def show_name(str, count):
    for i in range(count):
        print(str, i+1)


show_name("陈慧亿", 10)
