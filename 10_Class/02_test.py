# 2. 定义一个函数，函数参数为一个小于10000的正整数，分解它的各位数字，并以一个元组的形式返回。
# 在主程序中输入任意一个小于10000的正整数，借助调用该函数，输出它的各个组成数码的和。
# 例如，输入1234，输出1+2+3+4的和。

def sum_num(num):
    if num < 0 or num > 10000:
        print("你输入的数字有误！请输入一个小于10000的正整数")
        return
    # 千位
    kb = num // 1000
    # 百位
    hb = num // 100 % 10
    # 十位
    tb = num // 10 % 10
    # 个位
    ub = num % 10
    # 返回一个元组
    return (kb, hb, tb, ub)


num = int(input("请您输入一个(1-10000)的正整数数："))
tuple_num = sum_num(num)
result = 0
for i in tuple_num:
    result += i
    ll = 0
print("各个组成数码的和为：")
print(tuple_num[0], "+", tuple_num[1], "+", tuple_num[2], "+", tuple_num[3], "=", result)
