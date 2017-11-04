# -*- coding: utf-8 -*-
# 数组倒序，将列表进行颠倒
# 将第一个数与最后一个数进行比较

def reverseArr(list):
    def swap(list,i,j):
        list[i],list[j] = list[j],list[i]
    length = len(list)
    for i in range(int(length/2)):
        swap(list,i,length-i-1)
    return list
list  = [1,1,2,3,4,5,6,77,8]
print("the before is :{}".format(list))
print("the after is :{}".format(reverseArr(list)))

