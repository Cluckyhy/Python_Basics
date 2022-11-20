# （1）编写一个函数compare（file1,file2），比较两个文本文件内容是否相同，
# 如果内容相同返回True, 否则返回False。
# 在主程序中输入两个要比较的两文件名，然后调用以上函数进行比较。
# 如果文件内容相同则输出“No difference!”;
# 如果文件内容不相同，输出从第几个字符开始不相同。
# import os
#
# os.chdir(r"D:\JUFE_Second\Python_Class\Projects\11_Class\files");


def compare(filePath1, filePath2):
    # 读取文件1中的内容
    # 首先打开文件1
    file1 = open(filePath1, 'r', encoding='utf-8')
    # 读取文件1的内容，存放在text1中
    text1 = file1.read()
    # 关闭文件1
    file1.close()
    # 打开文件2
    file2 = open(filePath2, 'r', encoding='utf-8')
    # 读取文件2的内容，存放在text2中
    text2 = file2.read()
    # 关闭文件2
    file2.close()
    # 判断text1和text2是否相等
    if len(text1) != len(text2):
        return (False, "两文件内容长度不同")
    else:
        for i in range(0, len(text1)):
            if text1[i] != text2[i]:
                return (False, "文件内容不相同，从" + str(i + 1) + "个字符开始不相同")
        else:
            return (True, "No difference!")


# 主函数入口
if __name__ == '__main__':
    filePath1 = "files\\file1.txt"
    filePath2 = "files\\file2.txt"
    # 调用compare函数
    print("file1.txt文件和file2.txt中的内容是否相同?，答案如下：")
    print(compare(filePath1, filePath2))
