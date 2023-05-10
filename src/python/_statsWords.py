def getText():
    # 这是一个很老旧的打开文件方式，并不推荐
    txt = open("test.txt", "r").read()  # 以只读模式打开，不能修改，文件不存在，报错（异常）
    # 实际运行过程这个位置一直出错
    txt = txt.lower()  # 统一小写
    for i in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~"”“':
        txt = txt.replace(i, " ")  # 将各种分割作用（断句）的字符替换成空格
    return txt


def analyzeWords():
    # 枚举形式构建一个排除词汇库excludes来储存结果中不需要的词汇
    excludes = {"the", "and", "of", "you", "a", "i", "my", "in"}

    EngTxt = getText()
    words = EngTxt.split()  # 去除空格提取单词（方法作用是以空格（默认参数）为界限划分成一个个单词形式的字符串）

    counts = {}  # 新建一个空字典
    for word in words:
        # 对单词出现的频率进行统计 counts.get(word，0)方法封装了一个if-else语句：如果word在counts中，则返回word对应的值，如果word不在counts中，则返回0
        counts[word] = counts.get(word, 0) + 1
        # 所以上面的代码表示的是
    '''
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    '''
    for word in excludes:
        del (counts[word])  # 第四步删掉需要排除的词汇

    # 排序后输出，字典类型没有顺序，所以要转换为有顺序的列表类型，再用sort()方法排序
    items = list(counts.items())

    # sort()方法配合lambda函数实现根据单词次数对元素进行排序
    items.sort(key=lambda x: x[1], reverse=True)
    for item in items:
        word, count = item  # 返回相对应的键值对
        txt = open('word.txt', mode='a', encoding='utf-8')
        txt.write("{0:<10}{1:>5} \n".format(word, count))
