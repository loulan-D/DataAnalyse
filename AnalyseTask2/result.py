# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:36:18 2017

@author: loulan
"""
import pandas as pd
path = r"C:\Users\loulan\Documents\Tencent Files\67\FileRecv\201012学生成绩统计（已删除选课小于5的数据）.xls"
f = pd.read_excel(path)
f['KCCJ'][f['KSSJ']%1000//100 == 3] =60             #选出补考的学生，并把补考成绩改为60
f['KCCJ'][f['KSSJ']%1000//100 == 9] =60             # 补考一般是3月与9月
min_value = f.KCCJ.groupby([f['KCH'],f['KCM']]).min().to_frame()       # 每科成绩最小值
max_value = f.KCCJ.groupby([f['KCH'],f['KCM']]).max().to_frame()
mean_value = f.KCCJ.groupby([f['KCH'],f['KCM']]).mean().to_frame()
std_value = f.KCCJ.groupby([f['KCH'],f['KCM']]).std().to_frame()
result = pd.concat([min_value,max_value,mean_value,std_value],axis=1,join='inner')    #合并到一张表当中
result.columns =['MIN','MAX','MEAN','STD']
result.to_excel(r"C:\Users\loulan\Documents\Tencent Files\67\FileRecv\201012学生统计成绩汇总已考虑补考（每科最小值、最大值、平均值、平方差）.xls")