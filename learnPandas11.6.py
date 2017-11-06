# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:10:38 2017

@author: loulan
"""
# learn pandas 
from pandas import Series,DataFrame      #pandas 的两种数据结构  
import pandas as pd
import numpy as np

"""   Series
obj = Series([1,2,3,4])
obj.values   #表示形式
obj.index    #索引
obj1 = Series([1,2,3,4],index = ['a','b','c','d'])
obj1['a']               
obj1['a','b','c']          #通过索引选取值
obj1[obj1 >2]  
'a' in obj1
dicts = {'dong':112}
obj2 = Series(dicts)       #字典也可以转换为Series
#  pandas 的isnull 和notnull 可以用来表示缺失数据
pd.isnull(obj2)   #pd.notnull(obj2)
obj2.isnull ()    #Series也可以这样判断缺失数据

# Series 中一个最重要的功能是他在算术运算中会自动对齐不同索引的数据
# Series 的name 属性
obj2.name = "test"
obj2.index.name= "test"
obj2.columns.name= "test"

"""
"""
# 构造dataframe
data = {'name':['dong','jing','zhao','xi'],
        'nation':['china','japan','england','american'],
        'age':[22,22,22,44],
        'year':[1999,1998,1997,2000]}
frame = DataFrame(data,columns=['nation','age','name','year'],index = ['one','two','three','four'])  # 按指定的列序列进行排列
#查看列标签
frame.columns 
#获取一列的数据
print(frame.nation)
print(frame['age'])  

#获得一行的数据
#.loc for label based indexing or
#.iloc for positional indexing
print(frame.loc['one'])

#对列进行赋值   增加一个新列，并对其赋值
frame['country']  = ['henan','beijing','shanghai','sichuan']
print(frame)
frame['id']  = Series([12,13,14],index =['one','two','four'])
print(frame)

#del 删除列
del frame['id']
"""
"""
通过索引方式返回的列知识相应数据的视图，并不是副本，所以，对返回的Series所做的任何修改都会反映到源DataFrame上。
通过Series的copy方法可显示复制列
还有一种数据形式，就是嵌套字典
这样外层字典的键作为列，而内层字典的键作为行索引
frame.values
注：
frame的index对象是不可以修改的
"""


# 数据聚合与分组运算
"""
split-apply-combine   拆分-应用-合并  分组运算
axis = 0 行   axis = 1  列

"""
"""
      data1     data2 key1 key2
0  0.473087  0.233527    a  one
1 -0.127413 -0.202987    a  two
2  0.336374 -1.154539    b  one
3 -0.286923 -2.788686    b  two
4  2.347894 -2.578017    a  one
"""
df = DataFrame({'key1':['a','a','b','b','a'],
                'key2':['one','two','one','two','one'],
                'data1':np.random.randn(5),
                'data2':np.random.randn(5)})
# 按照key1分组，计算data1列的平均值  
grouped = df['data1'].groupby(df['key1'])
grouped1 = df['data1'].groupby([df['key1'],df['key2']])
print(grouped1.mean().unstack())
# 分组键可以是任意长度的数组
states = np.array(['beijing','shang','shang','beijing','beijing'])
years  = np.array([2005,2005,2006,2005,2006])
df['data1'].groupby([states,years]).mean()
print(df.groupby('key1').mean())
#  用groupby的size方法，它可以返回一个含有分组大小的Series：
a = df.groupby(['key1']).size()


























