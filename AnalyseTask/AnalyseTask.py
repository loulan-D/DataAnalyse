# -*- coding: utf-8 -*-
import zipfile        # 解压缩文件
import glob           # 筛选出所有的.xls文件
import os
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
import  shutil          #删除生成的临时文件

# 解压缩文件，解压到新生成的一个文件夹（2017集中采购表），并筛选出所有后缀名为.xls的文件
def unZipFile(path):
    f = zipfile.ZipFile(path + "合并数据练习.zip")   #解压缩文件
    f.extractall(path + "2017集中采购表")            #解压到一个新的文件夹
    path1 = path + '2017集中采购表'
    files = os.listdir(path1)
    fileList = []                                   # 所有符合要求的文件列表
    for file in files:
        xls  =os.path.join(path1,file) + '/*.xls'
        for filename in glob.glob(xls):
            fileList.append(filename)
    return  fileList

# 获取文件中的数据，并求出每个物品单价与数量的乘积，求出总额
def getData(path):
    fileList = unZipFile(path)
    os.mkdir(path+'temp')
    for i in range(len(fileList)):
        data = open_workbook(fileList[i])
        table = data.sheets()[0]
        rb = open_workbook(fileList[i])
        wb = copy(rb)
        s = wb.get_sheet(0)
        total_money = []
        str1  =os.path.splitext(fileList[i])[0]               # 将文件名与后缀.xls分隔开 目的获取文件名
        total_money.append(table.cell(5,2).value*159)         # 每个物品的数量乘以单价
        total_money.append(table.cell(5,4).value*158)
        total_money.append(table.cell(5,6).value*288)
        total_money.append(table.cell(5,8).value*178)
        total_money.append(table.cell(5,10).value*180)
        total_money.append(table.cell(5,12).value*368)
        s.write(5,0,int(i+1))                                # 序号
        s.write(5, 1, str1.split('-', 1)[1])                 # 分割出姓名
        s.write(5, 3, total_money[0])
        s.write(5, 5, total_money[1])
        s.write(5, 7, total_money[2])
        s.write(5, 9, total_money[3])
        s.write(5, 11, total_money[4])
        s.write(5, 13, total_money[5])
        s.write(5, 14, sum(total_money))
        wb.save(path +"temp/2017集中采购表{}.xls".format(i))
# 保存文件，获取最后结果，所有的.xls文件合并
def saveFile(path):
    os.mkdir(path + "2017集中采购表汇总")
    dataList = []
    fileList = os.listdir(path +"temp")
    path1 = path +"temp/"
    for file in fileList:
        file = open_workbook(path1 + file)
        table1 = file.sheets()[0]
        dataList.append(table1.row_values(5))
    commonInfo = []
    file1 = open_workbook(path1 + "2017集中采购表0.xls")
    table2 = file1.sheets()[0]
    file = xlwt.Workbook()  # 创建一个工作簿
    sheet = file.add_sheet('2017集中采购表', cell_overwrite_ok=True)  # 创建一个sheet
    for i in range(5):
        commonInfo.append(table2.row_values(i))
    for j in range(len(commonInfo)):
        for i in range(len(commonInfo[j])):
            sheet.write(j, i, commonInfo[j][i])
    file.save(path + "2017集中采购表汇总/2017集中采购表总表.xls")
    rXls  = open_workbook(path + "2017集中采购表汇总/2017集中采购表总表.xls")
    rSheet = rXls.sheets()[0]
    wXls = copy(rXls)
    sheetWrite = wXls.get_sheet(0)
    for m in range(5, len(dataList) + 5):
        for n in range(len(dataList[m - 5])):
            sheetWrite.write(m, n, dataList[m - 5][n])
    filename = path + "2017集中采购表汇总/2017集中采购表总表.xls"
    wXls.save(filename+ ".out"+os.path.splitext(filename)[-1])
    os.remove(filename)
    os.rename((filename+ ".out"+os.path.splitext(filename)[-1]),filename)

#删除临时文件
def deleteTemp(path):
    shutil.rmtree(path + "temp")
if __name__ == '__main__':
    path = "C:/Users/loulan/Desktop/"
    getData(path)
    saveFile(path)
    deleteTemp(path)

