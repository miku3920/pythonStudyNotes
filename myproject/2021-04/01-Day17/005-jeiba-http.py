import jieba
import jieba.analyse
import urllib.request as httplib

url="https://www.storm.mg/article/3575597"
req=httplib.Request(url)
reponse = httplib.urlopen(req)
contents=reponse.read().decode(reponse.headers.get_content_charset())
# jieba.analyse.set_stop_words("stop_words.txt")
dic = {}
keywords = jieba.analyse.extract_tags(contents, topK=100, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
for item in keywords:
    print(item[0], item[1])

print("="*40)
words =jieba.posseg.cut(contents)
for word, flag in words:
    if flag=="ns" or flag=="n" or flag=='vn' or flag=='n':
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] = dic[word] + 1

for w in sorted(dic, key=dic.get, reverse=True):
    if dic[w]>1:
        print("%s  %i " % (w, dic[w]))


