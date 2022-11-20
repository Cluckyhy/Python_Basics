# （4）编程求数列 1/2 + 2/3 + 3/5 + 5/8 + ....前30项之和
# 定义一个分子变量
fz = 1
# 定义一个分母变量
fm = 2
# 定义一个存放下一个分母的变量
nextFm = 0
# 定义一个总和变量
Sum = 0
# 定义一个计数器
count = 1
# 利用while循环求解此数列前30项之和
while count <= 30:
    Sum += fz / fm
    nextFm = fz + fm
    fz = fm
    fm = nextFm
    count = count + 1
print("数列 1/2 + 2/3 + 3/5 + 5/8 + ....前30项之和为：")
print(Sum)
