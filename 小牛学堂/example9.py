# -*- coding: utf-8 -*-
# 如果文件过大，有2GB，则该文件不适合一次性全部加载到内存

filename = r"D:\LearnPython\OpenCVPython\example7.txt"
map = {}
with open(filename) as fo:
    while True:
        line = fo.readline()
        if not line:break
        words = line.strip().split(" ")
        for word in words:
            map[word] = map.get(word,0) + 1
print(map)

"""
读取文件的三个方法，read()  readline()   readlines()
均可接收一个变量限制每次读取的数据量
read()
1.读取整个文件，将文件内容放到一个字符串变量中
2.如果文件大于可用内存，则不使用这个方法

readline()
1.每次读取一行，比readlines()慢的多
2.readline()返回的是一个字符串对象，保存当前行的内容

readlines()
1.一次性读取整个文件
2.自动将文件内容分析成一个行的列表

"""
