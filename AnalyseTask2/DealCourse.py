# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:06:47 2017

@author: loulan
"""
import pandas as pd
import matplotlib.pyplot as plt

## 选课人数分组统计图
#path = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩（41万）课程数.xls"  #从数据中分析得出的课程数文件
#f = pd.read_excel(path)
#bins = [0,5,100,1000,3000,5000,7000]                               #划分区间，选课人生小于5的课程、5到100的课程数 等
#groupName = ['小于5','5--100','100-1000','1000-3000','3000-5000','5000-7000']
#number = pd.cut(f.KCH,bins,labels = groupName).value_counts().to_frame()           # 基于41万条数据得出总的课程数
# #饼图的绘制
#sum1 = number.KCH.sum()                # 课程总数
#list1 = list(number.KCH)              
#labels= '100--1000','小于5','5--100','1000--3000','5000--7000','3000--5000'
#sizes = [list1[x]/sum1 for x in range(6)]
#explode = (0,0,0,0.1,0.2,0.15)
#plt.figure(figsize = (7,7))
#plt.pie(sizes,explode = explode,labels = labels,autopct = "%1.1f%%",shadow = False,startangle = 90)
#plt.title('课程选课人数统计图',fontsize=16,x=0.53,y=1.05,bbox={'facecolor':'0.8', 'pad':5})
#plt.text(0,-1.2,'注：占比情况表示为，选课人数所对应的课程数')
#plt.text(0,-1.3,'eg:小于5 即为选课人数小于5的课程在总课程中的占比')
#plt.savefig('课程选课人数统计饼图.jpg')
#plt.show()


 #标准差的统计图
 #成绩标准差  做一个 3以下的   4-6的  7-10的   10以上的
#path = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩41万学生统计成绩汇总已考虑补考（每科最小值、最大值、平均值、平方差）.xls"
#f = pd.read_excel(path)
#print("标准差中的最大值：{}".format(f.STD.max()))
#print("标准差中的最小值：{}".format(f.STD.min()))
#bins = [-0.3,3,6,10,33]
#groupName = ['3-','3--6','6--10','10+']
#number = pd.cut(f.STD,bins,labels = groupName).value_counts().to_frame()
#sum1 = number.STD.sum()
#list1 = list(number.STD)
#plt.figure(figsize = (8,8))
#labels= '6--10','10+','3--6','3-'
#sizes = [list1[x]/sum1 for x in range(4)]
#explode = (0,0.02,0,0.02)
#plt.pie(sizes,explode = explode,labels = labels,autopct = "%1.1f%%",shadow = False,startangle = 90)
#plt.title('课程成绩标准差范围统计',fontsize=16,x=0.53,y=1.05,bbox={'facecolor':'0.8', 'pad':5})
#plt.text(-0.5,-1.2,'示例：6--10  表示标准差范围')
#plt.text(-0.5,-1.3,'74.1% 表示成绩标准差范围在5到7之间的占所有课程成绩比')
#plt.text(-1.5,1.5,'标准差范围')
#plt.text(-1.1,1.5,'课程数(个)')
#plt.text(-1.5,1.4,'  10以上        114')
#plt.text(-1.5,1.3,'  6--10         664')
#plt.text(-1.5,1.2,'  3--6          110')
#plt.text(-1.5,1.1,'  3以下          8')
#plt.text(-1.5,1.0,'  总计          896')
#plt.savefig(r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\课程成绩标准差饼图.jpg")
#plt.show()


#
## 统计标准差大于28 和小于1的数据并保存到文件中
#path = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩41万学生统计成绩汇总已考虑补考（每科最小值、最大值、平均值、平方差）.xls"  # 已计算出标准差的数据表
#f = pd.read_excel(path)
#kchMore28 = list(f.loc[f.STD[f.STD>28].index.tolist()].KCH)       #标准差大于28对应的课程列表
#kchLess1 = list(f.loc[f.STD[f.STD<1].index.tolist()].KCH)         #标准差小于1对应的课程列表   
#path1 = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩（41万删除选课人数小于5的和英语四六级计算机考试等）.xlsx"
#f = pd.read_excel(path1)
#def selectDat(kch,std,str1):
#    index1 = []
#    for i in kch:
#       index1.append(f[f.KCH == i].index.tolist())
#    index2 = eval('[%s]'%repr(index1).replace('[', '').replace(']', '')) 
#    fdByStd = f.loc[index2]                                            #保存到文件中（标准差大于28的数据）
#    fdByStd.to_excel(r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩标准差{}于{}的原始数据.xlsx".format(str1,std))
#selectDat(kchMore28,28,'大')    # 标准差大于28对应的原始数据 文件
#selectDat(kchLess1,1,'小')      #标准差小于1对应的原始数据文件

# 统计那些离群课程的选课人数
#path1 = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩标准差大于28的原始数据.xlsx"
#f = pd.read_excel(path1)
#courses = f.KCH[f.KCH ==450006].value_counts()
#print(courses)


# 标准差为0的原始数据文件
#path = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩41万学生统计成绩汇总已考虑补考（每科最小值、最大值、平均值、平方差）.xls"  # 已计算出标准差的数据表
#f = pd.read_excel(path)
#kchLess0 = list(f.loc[f.STD[f.STD>13].index.tolist()].KCH)         #标准差为0对应的课程列表   
#path1 = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩(已删选课人数小于5的四六级的和将补考成绩置为60).xlsx"
#f = pd.read_excel(path1)
#def selectDat(kch):
#    index1 = []
#    for i in kch:
#       index1.append(f[f.KCH == i].index.tolist())
#    index2 = eval('[%s]'%repr(index1).replace('[', '').replace(']', '')) 
#    fdByStd = f.loc[index2]                                            #保存到文件中（标准差大于28的数据）
#    fdByStd.to_excel(r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩标准差大于13的原始数据.xlsx")
#    
#selectDat(kchLess0)


# 每一个学分各有多少课程实现代码
#path = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩（41万）.xlsx"
#f = pd.read_excel(path)
##xuefen = f.XF.value_counts().to_frame()
##xuefen.columns = ['NUMBER']
##xuefen.to_excel(r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩（41万）学分统计图.xlsx")
#xuefen = f.XF.groupby(f.KCM)
#course = f.KCSXDM[f.XF==0]
#print(course)



# 找出选课人数小于5的对应的课程号与课程名
#path = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩（41万）.xlsx"
#f = pd.read_excel(path)
#courses = f.KCH.value_counts()     #  课程数
#courLess1 = courses[courses <5].index.tolist()           
#def selectDat(kch):
#    index = []
#    for i in kch:
#        index1 = []
#        index1.append(f[f.KCH == i].index.tolist())
#        index3 = eval('[%s]'%repr(index1).replace('[', '').replace(']', ''))
#        index.append(index3[0])
##    index2 = eval('[%s]'%repr(index).replace('[', '').replace(']', '')) 
#    courNum = f.KCH.loc[index]
#    courName = f.KCM.loc[index]
#    result = pd.concat([courNum,courName],axis = 1,join = 'inner')
#    result.columns = ['KCH','KCM']
#    result.to_excel(r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级课程名对应课程号.xlsx")
#    
#selectDat(courLess1)


# 分类，将2010  2011  2012 级学生分开，分别统计不同学年的课程选课情况
#path = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩（41万）.xlsx"
#def differGradeCourse(path,grade):
#    f = pd.read_excel(path)
#    grades = f.NJDM[f.NJDM==grade].index.tolist()
#    course = f.loc[grades].KCH.value_counts()
#    course.to_excel(r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩{}课程数统计.xlsx".format(grade))
#for i in [2010,2011,2012]:
#    differGradeCourse(path,i)
    
 
 
# 不同学年课程选课人数统计图
#def drawPie(i):
#    path = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩{}课程数统计.xlsx".format(i)
#    f = pd.read_excel(path)
#    bins = [0,5,100,1000,2300]                               #划分区间，选课人生小于5的课程、5到100的课程数 等
#    groupName = ['小于5','5--100','100-1000','1000-2300']
#    number = pd.cut(f.KCH,bins,labels = groupName).value_counts().to_frame()           # 基于41万条数据得出总的课程数
#     #饼图的绘制
#    sum1 = number.KCH.sum()                # 课程总数
#    list1 = list(number.KCH)              
#    labels= '5--100','100--1000','小于5','1000--2300'
#    sizes = [list1[x]/sum1 for x in range(4)]
#    explode = (0,0,0,0)
#    plt.figure(figsize = (7,7))
#    plt.pie(sizes,explode = explode,labels = labels,autopct = "%1.1f%%",shadow = False,startangle = 90)
#    plt.title('{}学年课程选课人数统计图'.format(i),fontsize=16,x=0.53,y=1.05,bbox={'facecolor':'0.8', 'pad':5})
#    plt.text(0,-1.2,'注：占比情况表示为，选课人数所对应的课程数')
#    plt.text(0,-1.3,'eg:小于5 即为选课人数小于5的课程在总课程中的占比')
#    plt.savefig('{}学年课程选课人数统计饼图.jpg'.format(i))
#    plt.show()   
#lists = [2010,2011,2012]
#for i in lists:
#    drawPie(i)
    
# 复变函数的统计分析 从标准差大于13的文件中分离出复变函数的课程
#path = r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩标准差大于13的原始数据.xlsx"
#def differGradeCourse(path):
#    f = pd.read_excel(path)
#    grades = f.KCH[f.KCH==150668].index.tolist()
#    course = f.loc[grades]
#    course.to_excel(r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩复变函数统计课程数统计.xlsx")
#differGradeCourse(path)


# 分析复变函数课程的成绩 按班级号和考试时间进行划分
path  =r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩复变函数统计课程数统计.xlsx"
f = pd.read_excel(path)
min_value = f.KCCJ.groupby([f['BJH'],f['KSSJ']]).min().to_frame()
max_value = f.KCCJ.groupby([f['BJH'],f['KSSJ']]).max().to_frame()
mean_value = f.KCCJ.groupby([f['BJH'],f['KSSJ']]).mean().to_frame()
std_value = f.KCCJ.groupby([f['BJH'],f['KSSJ']]).std().to_frame()
result = pd.concat([min_value,max_value,mean_value,std_value],axis  = 1,join = 'inner')
result.columns =['MIN','MAX','MEAN','STD']
result.to_excel(r"C:\Users\loulan\Desktop\2012成绩处理\2017.11.12\201012级成绩复变函数最小值、最大值统计.xlsx")




