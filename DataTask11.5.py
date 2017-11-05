# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:55:11 2017

@author: loulan
"""
# 使用pandas库进行数据分析与处理  （因涉及隐私，数据文件不上传）
import pandas as pd
f = pd.read_excel(r"C:\Users\loulan\Documents\Tencent Files\670159498\FileRecv\201012级成绩.xls")   
list1 = [950004,950002,950005,950006,950021]         #这几个课程号的数据要删除，不具有一般性
"""
课程号
950002 大学英语四级考试
950004  NCRE一级考试
950005  NCRE二级c语言
950006   NCRE二级ACCESS
950021  NCRE一级MSoffice  校内
"""
# index 返回的是一个需要删除的几个课程号对应的索引值，然后进行删除
# f.drop(i)  里面的参数是行索引值   返回的是一个新的对象，不会对原来的对象进行修改，
# 而加一个参数inplace = True不会产生一个新的对象，直接对原来的对象进行修改。  
index = f[(f.KCH==950004)|(f.KCH==950002)|(f.KCH==950005)|(f.KCH==950006)|(f.KCH==950021)].index.tolist()
for i in index:
    f.drop(i,axis=0,inplace=True)

# 写出课程号和课程名称，人后把课程对应的平均值求出。即算该门成绩的平均值
data  = f.KCCJ.groupby([f['KCH'],f['KCM']]).mean()
data.to_excel(r"C:\Users\loulan\Documents\Tencent Files\670159498\FileRecv\201012级统计.xls")
