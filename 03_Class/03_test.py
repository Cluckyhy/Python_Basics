# 编写程序，实现货币的兑换，从键盘上输入人民币的币值，转换为美元的币值并输出
# 结果保留为2位小数，假设人民币兑换美元的汇率为0.1456，程序运行效果如下
money = input("请输入要兑换的人民币金额，以￥结束：")
num = money[0:-1]
# print(num)
# 将字符串转换为数值型
money2 = eval(num)
# print(money2)
dollar = money2 * 0.1456
dollar2 = round(dollar, 2)
print(money2, "元人民币可以兑换成", dollar2, "美元")
