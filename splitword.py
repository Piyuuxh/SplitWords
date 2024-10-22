def splitWord(words, sep):
    res = []
    for word in words:
        res.extend(i for i in word.split(sep) if i)
    return res

words = ['hello!','world!']
sep = '!'
print(splitWord(words, sep))