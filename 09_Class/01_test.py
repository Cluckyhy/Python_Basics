# 小明舍友的联系方式
dicTXT = {"小新": {"手机": "13913000001", "QQ": "18191220001"}, "小亮": {"手机": "13913000002", "QQ": "18191220002"},
          "小刚": {"手机": "13913000003", "QQ": "18191220003"}}
dicOther = {"大刘": {"手机": "13914000001", "QQ": "18191230001"}, "大王": {"手机": "13914000002", "QQ": "18191230002"},
            "大张": {"手机": "13914000003", "QQ": "18191230003"}}
dicTXT.update(dicOther)
dicWX = {"小新": "xx9907", "小刚": "gang1004", "大王": "jack_w", "大刘": "liu666"}

print("{:<5}".format("姓名") + "{:<13}".format("手机") + "{:<15}".format("QQ") + "{:<4}".format("微信"))
for key, value in dicTXT.items():
    if key in dicWX:
        value["微信"] = dicWX[key]
    else:
        value["微信"] = value["手机"]
    print("{:<5}".format(key), end="")
    for k, v in value.items():
        print("{:<15}".format(v), end="")
    print()

# 修改大王的手机号
dicTXT["大王"]["手机"] = "13914000004"

print("大王手机修改后：")
print("{:<5}".format("姓名") + "{:<13}".format("手机") + "{:<15}".format("QQ") + "{:<4}".format("微信"))
for key, value in dicTXT.items():
    if key in dicWX:
        value["微信"] = dicWX[key]
    else:
        value["微信"] = value["手机"]
    print("{:<5}".format(key), end="")
    for k, v in value.items():
        print("{:<15}".format(v), end="")
    print()

name = input("请输入姓名：")
info = dicTXT.get(name, "没有该同学的联系方式")
print(info)

