import wordcloud

file = open("txt\\三国演义.txt", encoding='utf-8')
text = file.read()
wc = wordcloud.WordCloud(font_path='C:\\Windows\\Fonts\\STXINGKA.TTF')
wc.generate(text)
image = wc.to_image()
image.show()