# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 11:50:15 2017

@author: loulan
"""
import pandas as pd
def selectDate(path):
    f = pd.read_excel(path)
    list1 = [950004,950002,950005,950006,950021]         #这几个课程号的数据要删除，不具有一般性（选课程号时得出的）
    students = f.XH.value_counts()     #  学生数
    courses = f.KCH.value_counts()     #  课程数
    courLess1 = courses[courses <5].index.tolist()   # 选课人数小于5的课程号
    courLess5 = courLess1 + list1          # 加上英语四级和计算机考试等  这是要删除的数据
    xuefen = f.XF.value_counts()
    print("每个学分各有多少课程，对所有的学生所有的课程\n{}".format(xuefen))
    print("共计有:\n{}个学生\n{}个课程 其中选课人数小于5的有{}个课程".format(len(students),len(courses),len(courLess5)))
    less5 = []                          #生成的list竟然是嵌套的list
    for i in courLess5:                 #找出选课人数小于5的课程号对应的索引坐标
        less5.append(f[f.KCH ==i].index.tolist())
    less = eval('[%s]'%repr(less5).replace('[', '').replace(']', ''))        
    for i in less:
        f.drop(i,axis =0,inplace=True)     #删除不符合要求的数据
    #path1 = r"C:\Users\loulan\Desktop\2012成绩处理\201012级成绩（6万）副本(删除选课人数小于5的和四级考试的).xlsx"
    path1 = r"C:\Users\loulan\Desktop\2012成绩处理\201012级成绩（41万）副本(删除选课人数小于5的和四级考试的).xlsx"
    f.to_excel(path1)
    return path1

def gradeAndResult(path1):
    f = pd.read_excel(path1)
    f['KCCJ'][f['KSSJ']%1000//100 == 3] =60
    f['KCCJ'][f['KSSJ']%1000//100 == 9] =60
    #学生成绩分组统计（每门课程最小值、最大值、平均分、标准差）  删除选课人数小于5人的数据。 
    min_value = f.KCCJ.groupby([f['KCH'],f['KCM']]).min().to_frame()
    max_value = f.KCCJ.groupby([f['KCH'],f['KCM']]).max().to_frame()
    mean_value = f.KCCJ.groupby([f['KCH'],f['KCM']]).mean().to_frame()
    std_value = f.KCCJ.groupby([f['KCH'],f['KCM']]).std().to_frame()
    result = pd.concat([min_value,max_value,mean_value,std_value],axis=1,join='inner')
    result.columns =['MIN','MAX','MEAN','STD']
    #result.to_excel(r"C:\Users\loulan\Desktop\2012成绩处理\201012级成绩（6万）副本学生统计成绩汇总已考虑补考（每科最小值、最大值、平均值、平方差）.xls")
    result.to_excel(r"C:\Users\loulan\Desktop\2012成绩处理\201012级成绩（41万）学生统计成绩汇总已考虑补考（每科最小值、最大值、平均值、平方差）.xls")
#path = r"C:\Users\loulan\Desktop\2012成绩处理\201012级成绩（6万）.xls"
path = r"C:\Users\loulan\Desktop\2012成绩处理\201012级成绩（41万）.xlsx"
path2 = selectDate(path)
gradeAndResult(path2)

