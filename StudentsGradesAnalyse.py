# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 14:28:22 2017

@author: loulan
"""

import pandas as pd
import os
from itertools import chain
import numpy as np
from openpyxl import Workbook           #  csv to xlsx   from stackoverflow
import csv                              #  csv to xlsx   from stackoverflow
import time

# 从原始文件中取前2万行作为测试
def selectPartOfAll(path):     
    f = pd.read_csv(path,encoding = 'utf-8')
    ff = f.head(20000)
    path1 = r"D:\task\houqin\testfile\test.csv"
    ff.to_csv(path1,encoding = 'utf-8')   # temp file 
    return path1

#从test 文件中筛选出网络缴费的数据
def selectNetJiaofei(path):
    f = pd.read_csv(path,encoding = 'utf-8')
    lists = f[f['对方户名']=='网络缴费'].index.tolist()
    netMoney = f.loc[lists]
    netMoney.to_csv(r"D:\task\houqin\testfile\netJiaofei.csv",encoding = 'utf-8')   # 把网络缴费的写到另一个文件中
    for i in lists:
        f.drop(i,axis = 0,inplace = True)
    path1 = r"D:\task\houqin\testfile\delNetJiaofei.csv"
    f.to_csv(path1,encoding = 'utf-8')     # 原数据文件，已删除网络缴费
    return path1     # 返回在原始文件中已删除网络缴费的文件  文件已减小许多

# "D:\task\houqin\testfile\delNetJiaofei.csv"  后续处理已删除网络缴费的这个文件
def shiTang(path):
    #从已经删除了网络缴费的数据的文件中分离出食堂的数据并保存到另一个文件shitang.csv文件中
    f = pd.read_csv(path,encoding = 'utf-8')
    listall = []
    #总文件中对方名称列表
    listMing = ['北区第一食堂','南区第一食堂','南区回民食堂','北区西式糕点','北区欧德隆快餐','北区台北牛肉拉面','北区味美麻辣香锅','北区山西风味','北区校园餐厅','北区一层水吧','北区学子居餐厅','北区大陷饺子','南区回民风味餐厅','北区美食美客','南区一食堂2层','南区第二食堂','北区清真食堂','南区福建风味','北区川鲁鄂美食城','北区二层豆浆','北区宜家餐厅','北区川鲁豫美食城']
    for ming in listMing:
        listall.append(f[f['对方户名']==ming].index.tolist())
    listAll = list(chain(*listall))      # 多维列表转换为一维列表
    eatMoney = f.loc[listAll]
    path1 = r"D:\task\houqin\testfile\shitang.csv"
    eatMoney.to_csv(path1,encoding = 'utf-8')
    return path1

#从食堂的数据中删除无关列，减小文件大小
def delNoneOfShiTang(path):
    ff = pd.read_csv(path,encoding = 'utf-8')
    ff.columns = ['1','2','3','本方户名','学号','事件名称','对方户名','交易额','流水时间']
    f = ff.drop(['1','2','3','事件名称'],axis = 1)  #drop，它不改变原有的df中的数据，而是返回一个dataframe来存放删除后的数据
    path1 = r"D:\task\houqin\testfile\shitang.csv"
    f.to_csv(path1,encoding = 'utf-8')
    return path1

#设置时间格式，将流水时间的日期格式设置为 正常的格式  并将日期列变为索引
def setTimeAsIndex(path):
    f = pd.read_csv(path,encoding = 'utf-8')
    f['流水时间'] = f['流水时间'].to_frame().applymap(np.int64)
    f['流水时间'] = f['流水时间'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d%H%M%S'))
    f = f.set_index('流水时间')
    path1 = r"D:\task\houqin\testfile\shitang.csv"
    f.to_csv(path1,encoding = 'utf-8')         # 新的文件，索引为日期列
    return path1

# 首先把每一年的数据分别保存到不同的文件中，后续分开处理  所有的年数据保存到yeardata文件夹中
def differYearOfShiTang(path):
    f = pd.read_csv(path,encoding = 'utf-8')
    f['流水时间'] = pd.to_datetime(f['流水时间'])
    f = f.set_index('流水时间')
    os.mkdir(r"D:\task\houqin\testfile\yeardata")    # 分开的每月的数据保存到这个文件夹中
    for i in [2013,2012,2015,2011,2014]:
        years = f[str(i)].index.tolist()
        data =f.loc[years]
        data.to_csv(r"D:\task\houqin\testfile\yeardata\data{}year.csv".format(i),encoding = 'utf-8')

def main1():
    path = r"D:\task\houqin\data.csv"
    path1 = selectNetJiaofei(selectPartOfAll(path))
    path2 = shiTang(path1)
    path3 = delNoneOfShiTang(path2)
    path4 = setTimeAsIndex(path3)
    differYearOfShiTang(path4)
#main1()
#  以上通过运行main()主函数实现功能：从原始数据中筛选出网络缴费的数据、筛选出食堂的数据、并将流水时间这一列设置为索引


# 因为本身前面已经划分好了年份，所以这里只需要考虑月份和中午的时间就可以了   
# 生成的新文件中包括  中午就餐的时间、姓名、学号、交易额
def differYear(year):
    os.mkdir(r"D:\task\houqin\testfile\{}monthdata".format(year))      
    path = r"D:\task\houqin\testfile\yeardata\data{}year.csv".format(year)
    f = pd.read_csv(path,encoding = 'utf-8')
    f['流水时间'] = pd.to_datetime(f['流水时间'])
    f = f.set_index('流水时间')
    for month in [1,3,4,5,6,9,10,11,12]:
        xuehaoResult = []
        moneyResultZhong = []
        xingmingResult = []
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]  # 为了方便处理，统一去一个月前28天 day is out of range for month
        for day in days:
            xuehao = f['{}-{}-{} 11:30:00'.format(year,month,day):'{}-{}-{} 13:30:00'.format(year,month,day)]['学号'].to_frame()
            xingming =f['{}-{}-{} 11:30:00'.format(year,month,day):'{}-{}-{} 13:30:00'.format(year,month,day)]['本方户名'].to_frame() 
            moneyzhong = f['{}-{}-{} 11:30:00'.format(year,month,day):'{}-{}-{} 13:30:00'.format(year,month,day)]['交易额'].abs().to_frame()
            moneyResultZhong.append(moneyzhong)
            xuehaoResult.append(xuehao)
            xingmingResult.append(xingming)
        xuehaoresult = pd.concat(xuehaoResult)
        moneyresultzhong = pd.concat(moneyResultZhong)
        xingresult = pd.concat(xingmingResult)
        result = pd.concat([xingresult,xuehaoresult,moneyresultzhong],axis = 1,join = 'outer')
        result.to_csv(r"D:\task\houqin\testfile\{}monthdata\data{}year{}month.csv".format(year,year,month),encoding = 'utf-8')

# 对前面生成的文件进行分析，最后一步，算出每月的中午消费的均值并保存到新的文件即最终的文件中
# 0   1   2    3    4  5  6  7    8
# 10  11  12   1    3  4  5  6    9 
def yearFinal(year):  
    path = r"D:\task\houqin\testfile\{}monthdata".format(year)
    filelist = os.listdir(path) 
    money = []
    for file in filelist:
        path = os.path.join(r"D:\task\houqin\testfile\{}monthdata".format(year),file)
        f = pd.read_csv(path,encoding = 'utf-8')
        money.append(((f['交易额'].groupby([f['本方户名'],f['学号']]).sum())/30).to_frame())
    result = pd.concat([money[3],money[4],money[5],money[6],money[7],money[8],money[0],money[1],money[2]],axis = 1,join = 'outer')
    result = result.fillna(0)
    result.columns = ['201101午','201103午','201104午','201105午','201106午','201109午','201110午','201111午','201112午']
    result.to_csv(r"D:\task\houqin\testfile\yearfinal\{}final.csv".format(year),encoding = 'utf-8',float_format = '%.3f')   # 小数点后保留三位

# 将前面生成的csv格式的文件转化为xlsx格式  because in my computer to open the csv is wrong
def csvToXlsx(year):
    wb = Workbook()
    ws = wb.active
    with open(r"D:\task\houqin\testfile\yearfinal\{}final.csv".format(year),'r',encoding = 'utf-8') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save(r"D:\task\houqin\testfile\yearfinals\{}final.xlsx".format(year))

# 把每一个文件的列索引改了：
def changeIndex():
    paths= r"D:\task\houqin\testfile\yearfinals"
    filelist = os.listdir(paths)
    os.mkdir(r"D:\task\houqin\testfile\yearfinalss")
    for file in filelist:       #11 12 13 14 15
        path = os.path.join(r"D:\task\houqin\testfile\yearfinals",file)
        year = int(str(file)[:4])
        f = pd.read_excel(path,encoding ='utf-8')
        f.columns = ['姓名','学号','{}01午'.format(year),'{}03午'.format(year),'{}04午'.format(year),'{}05午'.format(year),'{}06午'.format(year),'{}09午'.format(year),'{}10午'.format(year),'{}11午'.format(year),'{}12午'.format(year)]
        path1 = os.path.join(r"D:\task\houqin\testfile\yearfinalss",file)
        f.to_excel(path1,encoding = 'utf-8')

# 生成的最后的文件
def finalResult(path):    
    pathfiles = []
    for file in path:
        pathfile = os.path.join(r"D:\task\houqin\testfile\yearfinalss",file)
        pathfiles.append(pathfile)
    f1 = pd.read_excel(pathfiles[0])
    f2 = pd.read_excel(pathfiles[1])
    result1 = pd.merge(f1,f2,how = 'outer')
    result1.to_excel(r"D:\task\houqin\testfile\finalresult\resutl1.xlsx")
    
    f3 = pd.read_excel(pathfiles[2])
    f4 = pd.read_excel(r"D:\task\houqin\testfile\finalresult\resutl1.xlsx")
    result2 = pd.merge(f4,f3,how = 'outer')
    result2.to_excel(r"D:\task\houqin\testfile\finalresult\resutl2.xlsx")
    
    f5 = pd.read_excel(pathfiles[3])
    f6 = pd.read_excel(r"D:\task\houqin\testfile\finalresult\resutl2.xlsx")
    result3 = pd.merge(f6,f5,how = 'outer')
    result3.to_excel(r"D:\task\houqin\testfile\finalresult\resutl3.xlsx")
    
    f7 = pd.read_excel(pathfiles[4])
    f8 = pd.read_excel(r"D:\task\houqin\testfile\finalresult\resutl3.xlsx")
    result4 = pd.merge(f8,f7,how = 'outer')
    result4.to_excel(r"D:\task\houqin\testfile\finalresutl.xlsx")

def main():
    years = [2011,2012,2013,2014,2015]
    for year in years:  #
        differYear(year)         # 直接传参   每一年不同月的午餐数据  2011  2012  2013  2014  2015
        time.sleep(6)
    os.mkdir(r"D:\task\houqin\testfile\yearfinal")
    for year in years:#
        yearFinal(year)         #  2011  2012  2013  2014  2015
        time.sleep(5)
    os.mkdir(r"D:\task\houqin\testfile\yearfinals")
    for year in years:
        csvToXlsx(year)
        time.sleep(5)
    changeIndex()
    path = r"D:\task\houqin\testfile\yearfinalss"
    paths = os.listdir(path)     #2011 2012 2013 2014 2015
    os.mkdir(r"D:\task\houqin\testfile\finalresult") 
    finalResult(paths)
main()



















