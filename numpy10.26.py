# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:09:27 2017
@author: loulan
@python-version: python3.6
<python数据分析学习基础教程，numpy学习指南> 学习笔记
"""

# how to save a file
import  numpy as np
from  datetime import datetime

# arr = np.eye(3)
# np.savetxt('test.txt',arr)        # np.savetxt()进行简单的写文件操作
c,v = np.loadtxt('data.csv',delimiter=',',usecols=(6,7),unpack=True)  #不同列的数据分开存储
def datestr2num(s):
    return datetime.strptime(s,"%d-%m-%y").date().weekday()
dates, close = np.loadtxt('data.csv',delimiter=',',usecols=(1,6),converters={1:datestr2num},unpack=True)
print("dates = {}".format(dates))
# averages = np.zeros(5)
# for i in range(5):
#     indices = np.where(dates ==i)
#     prices = np.take(close,indices)
#     avg = np.mean(prices)
#     print("day{},prices{},average{}".format(i,prices,avg))
#     averages[i]  = avg

top = np.max(averages)
print(top)
bottom = np.min(averages)
print(bottom)


