# 4、假设有三个列表：listwho=[‘小马’，‘小羊’，‘小鹿’]，
# listwhere=[‘草地上’，‘电影院’，‘家里’]，listwhat=[‘看电影’，‘听故事’，‘吃晚饭’]。
# 编写程序，随机生成三个0~2范围内的整数，将其作为索引访问三个列表中的对应元素，然后进行造句。
# 例如，随机生成的三个整数为1，0，2，则输出句子“小羊在草地上吃晚饭”。

from random import randint

listWho = ["小马", "小羊", "小鹿"]
listWhere = ["草地上", "电影院", "家里"]
listWhat = ["看电影", "听故事", "吃晚饭"]
index = randint(0, 2)
str1 = listWho[index]
str2 = listWhere[index]
str3 = listWhat[index]
print(str1+"在"+str2+str3)
