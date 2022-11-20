# 1.找一篇你感兴趣的中文文章（新闻、论文、小说均可，不小于1000字），进行词频统计并绘制词云图。
import jieba
import wordcloud
import jieba.posseg as psg


# 编写一个函数来读取文本内容
def getText(filePath):
    file = open('txt\\三国演义.txt', encoding='utf-8')
    text = file.read()
    file.close()
    return text


# 定义一个停用词表
def stopwordList(filePath):
    stopwords = [line.strip() for line in open(filePath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 编写一个函数对读取到的文本进行分词，并统计词频
def wordFreq(filepath, text, num):
    # 首先理由jieba库中的lcut()对文本进行分词
    words = jieba.lcut(text)
    # 创建一个统计分词出现次数的字典
    counts = {}
    # 排除文章中大意无关的词语，调用stopwordList()函数，得到一个sropword列表
    stopword = stopwordList('txt\\stop_word.txt')
    # 利用for循环，将每个分词添加到字典中
    for word in words:
        # 把字符长度为1的去除
        if len(word) == 1:
            continue
        elif word not in stopword:
            counts[word] = counts.get(word, 0) + 1
    # 将字典转换为列表后，对分词出现次数的排序
    items = list(counts.items())
    # 将列表以分词出现次数排序
    items.sort(key=lambda x: x[1], reverse=True)
    # 指定一个保存词频数的文件
    tofile = open(filepath[:-4] + '_词频.txt', 'w', encoding='utf-8')
    for i in range(num):
        word, count = items[i]
        tofile.writelines("{}\t{}\n".format(word, count))
    tofile.close()


# 编写一个获得文本中所有名词词性的列表
def getPos(filePath, posName):
    # 以读的方式打开文件
    file = open(filePath, 'r', encoding='utf-8')
    # 获取文本内容
    text = file.read()
    # 关闭文件
    file.close()
    # 根据指定文本词性得到分词列表
    seg = psg.cut(text)
    # 如果要获得名词
    if posName == 'noun':
        nounList = [x.word for x in seg if x.flag == 'n']
        return nounList
    # 如果要获得形容词
    if posName == 'adj':
        adjList = [x.word for x in seg if x.flag == 'a']
        return adjList
    # 如果要获得动词
    if posName == 'verb':
        verbList = [x.word for x in seg if x.flag == 'v']
        return verbList


# 编写一个函数对获取到的词性文本，进行统计
def PosFreq(fileName, PosList, num):
    # 定义一个统计个数的字典
    counts = {}
    # 利用循环进行遍历每一个词出现的个数
    for word in PosList:
        if len(word) == 1:
            continue
        counts[word] = counts.get(word, 0) + 1
    # 将字典转换为列表，进行排序
    items = list(counts.items())
    # 排序
    items.sort(key=lambda x: x[1], reverse=True)
    # 将得到的列表写到文件中
    tofile = open(fileName + '_词频.txt', 'w', encoding='utf-8')
    for i in range(num):
        word, count = items[i]
        tofile.writelines("{}\t{}\n".format(word, count))
    tofile.close()


# 编写一个绘制词云函数
def wdCloud(filePath):
    file = open(filePath, 'r', encoding='utf-8')
    text = file.read()
    wc = wordcloud.WordCloud(font_path='C:\\Windows\\Fonts\\STXINGKA.TTF', background_color='white',
                             width=800, height=600, max_words=50, margin=2)
    # 根据指定的text文本生成词云
    wc.generate(text)
    wc.to_file(filePath[:-4] + "cloud.png")
    file.close()


if __name__ == '__main__':
    text = getText('txt\\三国演义.txt')
    wordFreq("三国演义.txt", text, 50)
    wdCloud('三国演义_词频.txt')

    # 得到一个名词词频文件
    nounList = getPos('txt\\三国演义.txt', 'noun')
    PosFreq('名词', nounList, 50)
    wdCloud("名词_词频.txt")

    # 得到一个形容词词频文件
    adjList = getPos('txt\\三国演义.txt', 'adj')
    PosFreq('形容词', adjList, 50)
    wdCloud("形容词_词频.txt")

    # 得到一个动词词频文件
    verbList = getPos('txt\\三国演义.txt', 'verb')
    PosFreq('动词', verbList, 50)
    wdCloud("动词_词频.txt")

    print("执行完毕")
