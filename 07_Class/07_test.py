# 1.列表切片练习。创建一个包括你自己以及前后五名同学的学号列表（共11个学号），分别进行下面的切片操作：
# (1) 取最前3个学号
# (2) 取最后4个学号
# (3) 从索引3开始，连续取5个学号
# (4) 取索引为偶数的学号
# (5) 取你自己以及前后各一名同学的学号

studentSno = ["01", "02", "03", "04", "05", "5210763", "06", "07", "08", "09", "10"]
print("全部学号列表如下：")
print(studentSno)
print("最前3个学号为：", studentSno[0:3])
print("最后4个学号为：", studentSno[-4:])
index = 3
print("从索引为3开始，连续取5个学号为：", studentSno[index:index + 5])
print("索引为偶数的学号为：", studentSno[0::2])
strSno = input("请输入你的学号：")
if strSno not in studentSno:
    print("你输入的学号不存在！")
else:
    indexSelf = studentSno.index(strSno)
    print("你的学号为：" + studentSno[indexSelf] + "\t你的前一个学号为：" + studentSno[indexSelf - 1] + "\t你的后一个学号为：" + studentSno[
        indexSelf + 1])
