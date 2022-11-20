print('Chen')
print("'Hui'慧")
print('''"Python程序设计"
"C++程序设计"''')

# 字符串的索引与切片
# Python中字符串也提供区间访问方式，采用[头下标:尾下标]的方式，这种访问方式称为"切片"
# 若有字符串s,s[头下标:尾下标]表示在字符串s中取索引值从头下标到尾下标(不包含尾下标)的子字符串
# 切片方式中，若头下标缺省，表示从开始取子字符串；若尾下标缺省，表示取到最后一个字符；若头下标和尾下标均缺省，则直接取整个字符串
s = 'Hello Mike'
print(s[0], s[-1], s[8], s[-2])
print(s[0:5], s[6:-1])
print(s[:5], s[6:])
print(s[:])

# 内置的字符串运算符
print("AB" + "123")
print("Tom" * 3)
print("H" in "Hello")
print("h" in "Hello")

# 内置的字符串处理函数
x = "好好学习，天天向上"
print(len(x))
print(str(125))
print(str(3 + 5))
print(hex(62))
print(oct(62))
print(ord('/'),ord('+'),ord(' '))
print(chr(100),chr(97))
