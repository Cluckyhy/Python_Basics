# 输入一串字符串：Hi,This is the first Python program
s = input("输入一串字符串：")
# 统计字符个数
num = len(s)
print("字符串个数为：", num)
# 最大字符
maxS = max(s)
print("字符中最大的字符为：", maxS)
# 最小字符
minS = min(s)
print("字符中最小的字符为：", minS)
# 所有字母大写
upperS = s.upper()
print("字符串大写后：", upperS)
# 所有字母小写
lowerS = s.lower()
print("字符小写后：", lowerS)
# 交换字母的大小写
swapS = s.swapcase()
print("交换字母大小写后：", swapS)
# 每个首字母大写，其余小写
fUpper = s.title()
print("首字母大写，其余小写后：", fUpper)
# 查找单词的Python的位置
findS = s.find("Python")
print("字符中的Python的位置是：", findS)


