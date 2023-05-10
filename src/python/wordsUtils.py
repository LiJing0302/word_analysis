from textblob import TextBlob
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re

data = "At eight o'clock on Thursday morning  Arthur didn't feel very good."


# 文本单词纠正
def correctText(str):
    output = TextBlob(data).correct()
    return output


# 使用 NLTK 和 TextBlob 的词标记化
def getWordToken():
    text = open('test.txt', 'r').read()
    text = re.split(r'\s+', text)
    counts = {}  # 新建一个空字典
    pattern = r"[，。！？“”‘’：；·、（）【】]|[,.?!;():/-]|[0-9]|—"
    for item in text:
        if (re.search(pattern, item) is None):
            # item = item.strip()
            item = item.lower()  # 统一小写
            counts[item] = counts.get(item, 0) + 1

    # 排序后输出，字典类型没有顺序，所以要转换为有顺序的列表类型，再用sort()方法排序
    words = list(counts.items())
    # sort()方法配合lambda函数实现根据单词次数对元素进行排序
    words.sort(key=lambda x: x[1], reverse=True)
    for item in words:
        word, count = item  # 返回相对应的键值对
        txt = open('./word.txt', mode='a', encoding='utf-8')
        txt.write("{0:<10}{1:>5} \n".format(word, count))

    # nltk_output = nltk.word_tokenize(text)
    # textblob_output = TextBlob(data).words
    # txt = open('./word.txt', mode='a', encoding='utf-8')
    # for item in text:
    #     txt.write(item+'\n')
