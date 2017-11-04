# -*- coding: utf-8 -*-
# 排序算法，选择排序
# 把第一个元素依次和后面的所有元素进行比较，第一次结束后，就会有最小的值出现在最前面

def selectSort(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j] = list[j],list[i]
    return list
list = [1,2,6,3,4,7,3,8,10,12,17,11,19,14]
print(selectSort(list))

