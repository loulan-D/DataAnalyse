# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:55:11 2017
@author: xiaodong2012
"""
# 使用pandas库进行数据分析与处理  （因涉及隐私，数据文件不上传）
import pandas as pd
f = pd.read_excel(r"C:\Users\loulan\Documents\Tencent Files\67\FileRecv\201012级成绩.xls")   
list1 = [950004,950002,950005,950006,950021]         #这几个课程号的数据要删除，不具有一般性
students = f.XH.value_counts()                       #统计学号 既可以得到学生数
courses = f.KCH.value_counts()                       #统计课程
courLess1 = courses[courses <5].index.tolist()       # 选课人数小于5的课程号
courLess5 = courLess1 + list1                        # 加上英语四级和计算机考试等  这是要删除的数据
xuefen = f.XF.value_counts()                         #学分的统计
print("每个学分各有多少课程，对所有的学生所有的课程\n{}".format(xuefen))
print("共计有:\n{}个学生\n{}个课程 其中选课人数小于5的有{}个课程".format(len(students),len(courses),len(courLess5)))

# less5 返回的是一个需要删除的几个课程号对应的索引值，然后进行删除
# f.drop(i)  里面的参数是行索引值   返回的是一个新的对象，不会对原来的对象进行修改，
# 而加一个参数inplace = True不会产生一个新的对象，直接对原来的对象进行修改。  
less5 = []                                            #生成的list竟然是嵌套的list
for i in courLess5:                                   #找出选课人数小于5的课程号对应的索引坐标
    less5.append(f[f.KCH ==i].index.tolist())
less = eval('[%s]'%repr(less5).replace('[', '').replace(']', ''))        
for i in less:
    f.drop(i,axis =0,inplace=True)                    #删除不符合要求的数据
f.to_excel(r"C:\Users\loulan\Documents\Tencent Files\67\FileRecv\201012学生成绩统计（已删除选课小于5的数据）.xls")

"""
课程号  这是统计出课程数之后得出的，选择这几个课程的课程号，删除用
950002 大学英语四级考试
950004  NCRE一级考试
950005  NCRE二级c语言
950006   NCRE二级ACCESS
950021  NCRE一级MSoffice  校内
"""