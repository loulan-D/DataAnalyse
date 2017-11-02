# -*- coding: utf-8 -*-
# 单词计数，统计出demo文本中所有出现的单词的出现次数

map = {}
filename = "D:/LearnPython/OpenCVPython/example7.txt"
with open(filename) as fo:
    for line in fo.readlines():
        words = line.strip().split(" ")
        for word in words:
            map[word] = map.get(word,0) +1
print(map)

"""
Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
dict.get(key,default = None)
default -- 如果指定键的值不存在时，返回该默认值值
"""
"""
python中字符串strip方法
Python字符串strip()方法返回从字符串的开始和结束(默认空格字符)中删除指定所有字符的字符串的副本。
str.strip([chars])
chars :要从字符串的开头或结尾移除的字符。
str = "***hello world  ni hao ya ****"
print(str.strip('*'))
"""
