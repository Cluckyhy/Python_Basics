# 3. 身体质量指数（简称体质指数又称体重指数，英文为Body Mass Index，简称BMI），
# 是用体重公斤数除以身高米数平方得出的数字，是国际上常用的衡量人体胖瘦程度以及是否健康的一个标准。
# BMI值的不同反映了不同的肥胖程度，其对应关系如下：
# 偏瘦：      BMI指数 < 18
# 正常体重：  BMI指数 = 18 - 25
# 超重：      BMI指数 = 25 - 30
# 轻度肥胖：  BMI指数 = 30 - 35
# 中度肥胖：  BMI指数 = 35 - 40
# 重度肥胖：  BMI指数 > =40
# 请编写一个函数getBMI，它通过两个参数获得身高和体重，并返回一个由BMI数值和肥胖程度字符串两个元素构成的元组。
# 在主程序中由用户输入身高和体重，通过调用自己编写的这个getBMI函数，打印BMI计算结果。

def get_BMI(height, weight):
    bmi = weight // height ** 2
    if bmi < 18:
        return (bmi, "偏瘦")
    elif bmi < 25:
        return (bmi, "正常体重")
    elif bmi < 30:
        return (bmi, "超重")
    elif bmi < 35:
        return (bmi, "轻度肥胖")
    elif bmi < 40:
        return (bmi, "中度肥胖")
    else:
        return (bmi, "重度肥胖")


weight = int(input("请输入您的体重(公斤)："))
height = float(input("请输入您的身高(米)："))

tuple_bmi = get_BMI(height, weight)
print("您的身高是{}, 体重是{}, BMI指数为{}, 肥胖程度为：{}".format(height, weight, tuple_bmi[0], tuple_bmi[1]))
