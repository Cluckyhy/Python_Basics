# （3）某心理测试题全部由单选题组成，每个题目有3个选项，不同选项得分不同（但每题分数都是在10分-99分之间），
# 答案和分数保存在一个文件answer.txt中，格式为：
# 1A10B20C30
# 2A20B10C30
# 3A10B30C20
# 4A20B30C10
# 5A30B20C40
# 6A20B40C10
# ……
# 20A10B30C50
# 其中最左边的数字为题号，其后是该题各选项的分数。
# 从键盘输入某位考生答案，例如：
# ABCCBABCAABACBCABCBC
# 编程计算并输出该考生的成绩。

# 有多位学生参加了考试，
# 他们的答案保存在另一个文件result.txt中，例如：
# 20190322 : ABCCBACBBCABCBCBACAB
# 20190342 : CBCACBCBBACBBBCAAACB
# 20190362 : BACBACBBCACBACABCBAA
# 20190122 : CBBABCAACBCBACBAACBC
# ……
# 其中冒号左边的数字为学生学号，冒号右边的字母依次为该生1至20题的答案。
# 假设所有学生学号长度相同，编程计算所有考生的成绩，并将他们的成绩在一个新文件score.txt中保存，格式如下：
# 20190322的得分:293分
# 20190342的得分: 328分
# 20190362的得分: 294分
# 20190122的得分: 146分
import os

os.chdir(r"D:\JUFE_Second\Python_Class\Projects\11_Class\files");


def calculateScore(answer):
    # 打开文件
    file = open("answer.txt", 'r', encoding='utf-8')
    # 读取文件信息
    listScore = file.readlines()
    # 创建一个外字典
    dic_Item = {}
    # 创建一个内字典
    dic_Score = {}
    # 遍历listScore
    for item in listScore:
        # 找到 A
        titleNo = 0
        for i in range(0, len(item)):
            if item[i] == "A":
                # 题号
                titleNo = eval(item[0: i])
                # 分数A
                scoreA = eval(item[i + 1: i + 3])
                # 分数B
                scoreB = eval(item[i + 4: i + 6])
                # 分数C
                scoreC = eval(item[i + 7: i + 9])
                # 把各分数放入到内字典中
                dic_Score = {'A': scoreA, 'B': scoreB, 'C': scoreC}
            # 把每一题的内容放入到外字典中
            dic_Item[titleNo] = dic_Score
    # 关闭文件
    file.close()

    # 通过考生答案计算考生总成绩
    titleNum = 1
    sumScore = 0
    for ch in answer:
        sumScore += dic_Item[titleNum][ch]
        titleNum += 1
    return sumScore


def storeScore():
    # 打开文件
    file = open("result.txt", 'r', encoding='utf-8')
    # 读取文件信息
    listAnswer = file.readlines()
    # 定义一个字典存放学生答案
    dic_answer = {}
    # 遍历取出每个学生的答案，并将答案存放到字典中
    for item in listAnswer:
        line = item.strip('\n')
        list = line.split(' : ')
        # 调用calculateScore()函数计算每个学生的成绩
        scoreSum = calculateScore(list[1])
        dic_answer[list[0]] = scoreSum
    # 打开文件
    file1 = open("score.txt", 'w', encoding='utf-8')
    # 写入信息到文件中
    for i in dic_answer.keys():
        s = i + "的得分为：" + str(dic_answer[i]) + "分" + "\n"
        file1.write(s)
    # 关闭文件
    file.close()
    file1.close()


if __name__ == '__main__':
    answer = input("请输入考生答案(20题)：")
    print("该考生的总成绩为：", calculateScore(answer))
    print("已将指定文件中的学生答案的成绩保存在 score.txt文件中，请自行查看...")
    # 调用存储分数函数
    storeScore()
