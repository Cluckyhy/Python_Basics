# 1、编写程序，将用户输入的英文句子中的单词（忽略标点符号）进行逆序排列后输出。
# 例如：输入“How are you”,则程序输出“you are how”。

str = input("请输入英文句子：")
sentenceList = str.split(" ")
# print(sentenceList)
print("逆序排列后的结果为：")
for item in range(len(sentenceList) - 1, -1, -1):
    # print(item)
    print(sentenceList[item], end=" ")
