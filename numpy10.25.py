# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:09:27 2017
@author: loulan
@python-version: python3.6
<python数据分析学习基础教程，numpy学习指南> 学习笔记
"""

#用python循环和用numpy之比较

#import numpy as np
#def pythonsum(n):
#    """
#    注意range()的使用，开始时用a = range(n) ,error,
#    错误信息：TypeError: 'range' object does not support item assignment
#    注意range()返回的是range object 而不是list
#    通过强制类型转换，转换为list
#    """
#    a = list(range(n))
#    b = list(range(n))
#    c = []
#    
#    for i in range(n):
#        a[i] = i ** 2
#        b[i] = i ** 3
#        c.append(a[i]+b[i])
#    return c
#    
#def numpysum(n):
#    a = np.arange(n) **2
#    b = np.arange(n) **3
#    c = a+b
#    return c
#
#print(pythonsum(5))
#print(numpysum(5))
    
#以微秒的精度分别记录pythonsum()和numpysum()的耗时
import sys
from datetime import datetime
import numpy as np

def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []
    
    for i in range(n):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i]+b[i])
    return c
    
def numpysum(n):
    a = np.arange(n) **2
    b = np.arange(n) **3
    c = a+b
    return c

n = 2000

start1 = datetime.now()
pythonsum(n)
time1 = datetime.now() - start1
print("pythonsum slapsed time in microseconds {}".format(time1.microseconds))

start2 = datetime.now()
numpysum(n)
time2 = datetime.now() - start2
print("numpysum slapsed time in microseconds {}".format(time2.microseconds))






































