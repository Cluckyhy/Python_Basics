# （2）有一个文本文件student.txt，其中包含了学生的学号，格式如下。
# 154772  154778  154784  154793  156273  ……
# 假设现在老师要随机点几位学生回答问题。编写一个函数，每次调用从中抽取一位学生。
# 在主程序中对其连续调用，并可以控制是否需要继续抽取。假设每次抽取的学生可以重复。
# 如果老师要随机从所有学生中点3位学生回答问题。（学号不重复）
import os
os.chdir(r"D:\JUFE_Second\Python_Class\Projects\11_Class\files");

from random import *


def randSno():
    # 打开文件
    file = open("student.txt", 'r', encoding='utf-8')
    # 读取文件信息
    listSno = file.read().split(" ")
    print("共有学生：")
    for item in listSno:
        print(item, end=" ")
    # 随机抽取学生
    randNum = randint(0, len(listSno) - 1)
    print("\n抽取到的学生为：", listSno[randNum])
    # 关闭文件
    file.close()


def randThree():
    # 打开文件
    file = open("student.txt", 'r', encoding='utf-8')
    # 读取文件信息
    listSno = file.read().split(" ")
    print("共有学生：")
    for item in listSno:
        print(item, end=" ")
    print()
    # 随机抽取三名学生，并且不能重复
    listThree = []
    while True:
        randNum = randint(0, len(listSno) - 1)
        if listSno[randNum] not in listThree:
            listThree.append(listSno[randNum])
        if len(listThree) == 3:
            break;
    print("抽取的三名学生为[不带重复]：")
    for i in listThree:
        print(i, end=" ")
    # 关闭文件
    file.close()


if __name__ == '__main__':
    print("-------------1、随 机 抽 取 一 位 学 生    -------------")
    print("-------------2、随机抽取三位位学生[不带重复]-------------")
    option = input("请输入您的选择：")
    if option == "1":
        randSno()
        while True:
            isGo = input("是否继续抽取[Y/N]：").upper()
            if isGo == "Y":
                randSno()
            else:
                print("不再抽取，程序退出...")
                break;
    else:
        randThree()