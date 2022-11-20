# （5）输入任意一串字符，输出不属于英文单词“python”中的字符之一的那些字符。
# 例如：输入“thank  you”, 输出“ak  u”
str = input("请输入任意一串字符：")
print("不属于英文单词Python的有：")
for char in str:
    if char not in "Python":
        print(char, end="")
