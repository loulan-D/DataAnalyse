# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:06:47 2017

@author: loulan
"""
import pandas as pd
import matplotlib.pyplot as plt

# 课程数的统计
#path = r"C:\Users\loulan\Desktop\2012成绩处理\201012级成绩（41万）课程数.xls"
#f = pd.read_excel(path)
#bins = [0,5,100,1000,3000,5000,7000]
#groupName = ['小于5','5--100','100-1000','1000-3000','3000-5000','5000-7000']
#number = pd.cut(f.KCH,bins,labels = groupName).value_counts().to_frame()
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

# 标准差的统计
path = r"C:\Users\loulan\Desktop\2012成绩处理\201012级成绩（41万）学生统计成绩汇总已考虑补考（每科最小值、最大值、平均值、平方差）.xls"
f = pd.read_excel(path)
print("标准差中的最大值：{}".format(f.STD.max()))
print("标准差中的最小值：{}".format(f.STD.min()))
bins = [0,2,5,7,11,13,34]
groupName = ['0--2','2--5','5--7','7--11','11--13','13之上']
number = pd.cut(f.STD,bins,labels = groupName).value_counts().to_frame()
sum1 = number.STD.sum()
list1 = list(number.STD)
plt.figure(figsize = (8,8))
labels= '7--11','5--7','2--5','11--13','13+','0--2'
sizes = [list1[x]/sum1 for x in range(6)]
explode = (0,0,0,0,0.2,0.3)
plt.pie(sizes,explode = explode,labels = labels,autopct = "%1.1f%%",shadow = False,startangle = 90)
plt.title('每门课程成绩标准差范围统计',fontsize=16,x=0.53,y=1.05,bbox={'facecolor':'0.8', 'pad':5})
plt.text(0,-1.2,'示例：0--2  表示标准差范围')
plt.text(0,-1.3,'19.6% 表示成绩标准差范围在5到7之间的占所有课程成绩比')
plt.savefig('课程成绩标准差饼图.jpg')
plt.show()




