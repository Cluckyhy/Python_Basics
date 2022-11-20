# 班级总人数
total = 25
# 选修一号课程的同学有
subject1 = {"李雷", "张玉", "王晓刚", "陈红静", "方向", "司马清"}
# 选修二号课程的同学有
subject2 = {"施然", "李芳芳", "刘潇", "方向", "孙一航", "黄煌"}
# 选修三号课程的同学有
subject3 = {"陈红静", "方向", "刘培良", "张玉", "施小冉", "司马清"}

# 这个班有多少位同学没有选课
sumNum = subject1 | subject2 | subject3
print("这个班选课的同学有：")
print(sumNum)
print("有", total - len(sumNum), "个同学没有选课")

# 有多少位学生同时选修了2门课
obj1 = len(subject1 & subject2)
obj2 = len(subject1 & subject3)
obj3 = len(subject2 & subject3)
print("有", obj1 + obj2 + obj3, "个同学同时选修了2门或2门以上的课")

obj4 = subject1 & subject2 & subject3
print("有", len(obj4), "个同学同时选修了3门课")

print("有", len(sumNum) - len(obj4), "个同学只选修了1门课")
