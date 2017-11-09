# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:19:31 2017

@author: loulan
"""
# 异常处理的学习
# 异常处理机制： try语句定义代码块，以运行可能抛出饿异常的代码；通过except语句，捕获特定的异常并做相应的处理；通过finally保证正常运行
"""
自定义异常类一般继承Exception或其子类。自定义异常类的命名规则一般以Error或Exception 为后缀
创建自定义异常：
class NumberError(Exception):      #自定义异常类，继承与Exception
    def __init__(self,data):
        Exception.__init__(self,data)
        self.data = data
    def __str__(self):             #重载str方法
        return self.data + ":非法数值（<0）"
if __name__ =='__main__':
    raise NumberError('-123')

from NumberError import *
def average(data):
    sum = 0
    for i in data:
        if i<0: raise NumberError(str(i))
        sum += i
    return sum/len(data)
if __name__ = '__main__':
    data1 = (1,2,23,4)
    print("average = "+average(data1))
    data2 =(1,2,-9,3)
    print("average = "+average(data2))
"""
"""
from NumberError import *
from raise_exception import *
if __name=='__main__':
    try:
        data2 = (11,11,21,-11)
        print("result="+average(data2))
    except NumberError as e:
        print(e)
"""
# 要将带有具体的（派生类最高的）异常类的except 块放在最前面 
# 派生程度高的异常类NumberError放置在派生类低的Exception后面
try:
    f = open('example7.txt','w')
    while True:
        s = input("请输入字符串  按Q键结束")
        if s.upper()=='Q':break
        f.write(s+'\n')
except KeyboardInterrupt:
    print("程序中断ctrl + c")
finally:
    f.close()
    















