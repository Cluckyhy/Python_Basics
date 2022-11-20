# 创建6个元组，存放6名选手的评分
player1 = [90, 94, 97, 86, 85, 89, 88, 85]
player2 = [91, 91, 92, 98, 90, 96, 90, 95]
player3 = [96, 86, 97, 96, 87, 86, 86, 96]
player4 = [95, 95, 94, 93, 97, 98, 99, 95]
player5 = [95, 87, 94, 94, 93, 99, 96, 97]
player6 = [89, 97, 91, 95, 89, 94, 97, 92]

# 创建一个字典，按选手编号存放选手的评分
dic_Play = {"012": player1, "005": player2, "108": player3, "037": player4, "066": player5, "020": player6}
dic_finally = {}
for key, value in dic_Play.items():
    print(key, "选手成绩为：", value)
    print(key, "选手最高分为：", max(value))
    print(key, "选手最低分为：", min(value))
    # 去掉选手最高分
    value.remove(max(value))
    # 去掉选手最低分
    value.remove(min(value))
    print("去掉一个最高分和一个最低分后的成绩为：", value)
    # 求出各选手平均值
    average = sum(value) / len(value)
    print(key, "选手的平均值为：", average, "\n")
    # 将得到选手平均值后，存放到最后成绩字典中
    dic_finally[key] = average

# 利用列表生成器，生成(最后得分，选手编号)元组构成的列表
List_finally = [(v, k) for k, v in dic_finally.items()]
# 将列表中的元素按选手最后得分 由高到低排序
List_finally.sort(reverse=True)
print("编号：" + "\t" + "最后得分：")
for i in List_finally:
    print(i[1], "\t", "{:.1f}".format(i[0]))
