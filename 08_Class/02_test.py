# 2.编写程序，实现以下功能：
# （1）创建空字典dic_student
# （2）由用户依次输入五名学生的姓名和年龄，存入字典dic_student
# （3）输出字典dic_student中的内容，格式为：
# 王建   18
# 张云   19
# 张秋雨 18
# 刘欢   17
# 姜宇   19
# （注意，年龄数字是对齐的）
# （4）打印五名学生的最大年龄、最小年龄和平均年龄。

# 创建空字典 dic_student
dic_student = {}

for i in range(5):
    name = input("请用户输入姓名：")
    age = int(input("请用户输入年龄："))
    dic_student[name] = age

# 输出字典dic_student，遍历字典的整个条目
for item in dic_student.items():
    print(item[0] + "\t" + str(item[1]))

# 打印五名学生的最大年龄、最小年龄、平均年龄
# 依次遍历字典的value值，存放到一个ageList列表中
ageList = []
for value in dic_student.values():
    ageList.append(value)
# print(ageList)
# 最大年龄
print("五名学生的最大年龄为：", max(ageList))
print("五名学生的最小年龄为：", min(ageList))
print("五名学生的平均年龄为：", sum(ageList) / len(ageList))
