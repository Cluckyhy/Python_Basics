# 1、使用多重循环结构，编程输出如下图形
for i in range(7, 1, -1):
    for j in range(2 * i, 1, -1):
        print("*", end="")
    print()
