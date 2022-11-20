# 输入字符串 http://sports.sina.com.cn/
s = input("请输入字符串：")
# 字符串中字母t出现的次数
tc = s.count('t')
print("字符串中t出现的次数为：", tc)
# 字符串中com子字符串出现的位置
lc = s.find('com')
print("字符串中com出现的位置为：", lc)
# 将字符串中所有的.替换为-
sw = s.replace('.', '-')
print("将字符串中的.替换成-后的字符串为：", sw)
# 提取sports和sina两个子字符串(分别使用正向切片和反向切片方式)。
# 正向取sports
zsp = s[7:13]
print("正向取sports为：", zsp)
# 反向取sports
fsp = s[-19:-13]
print("反向取sports为：", fsp)
# 正向取sina
zsi = s[14:18]
print("正向取sina为：", zsi)
# 反向取sina
fsi = s[-12:-8]
print("反向取sina为：", fsi)
# 将字符串中的字母全变为大写
sUp = s.upper()
print("将字符串中的字母全变为大写为：", sUp)
# 输出字符串的总字符个数
sct = len(s)
print("字符串的总字符个数为：", sct)
# 在字符串后拼接子字符串"index"
snw = s+"index"
print('在字符串后拼接子字符串"index"为', snw)




