# 编写函数 avg(lst)，参数lst是一个列表，函数可以返回 lst 的整数平均值
# return int(sum(list)/len(lst)),调用avg(lst)函数求每个学生的平均值
# 已知成绩列表 s = {"小李":[77,54],"小张":[89,66,78,99],"小陈":[90],"小杨":[69,58,93]}
# 输出结果为：{'小李':65,'小张':83,'小陈':90,'小杨':73}

def avg(lst):
    return int(sum(lst) / len(lst))


# 定义字典储存各学生的成绩
dic_score = {"小李": [77, 54], "小张": [89, 66, 78, 99], "小陈": [90], "小杨": [69, 58, 93]}

# 遍历取出字典中的成绩信息
for key, score_lst in dic_score.items():
    dic_score[key] = avg(score_lst)

# 输出结果
print("每个学生的平均分结果如下：")
for key, value in dic_score.items():
    print(key, ":", value, end="\t")
