# -*- coding: utf-8 -*-
"""
2 分查找
用 2 分法快速在有序列表中找到指定元素在列表中的角标， 若没有找到则返回-插入点-1(<0)的值
例如：
在有序列表 list1 中[1, 3, 8, 12, 23, 31, 37, 42, 48, 58]中查找值为 8 的记录的。
在有序列表 list1 中[1, 3, 8, 12, 23, 31, 37, 42, 48, 58]中查找值为 9(不存在， 以负数形式返回插入点的位置)的记录。
"""
def bianrySearch(list,value):
    low = 0
    high = len(list)-1
    mid = (low + high)/2
    while low <= high:
        if list[int(mid)] == value:
            return int(mid)
        elif list[(int(mid))] > value:
            high = int(mid) -1
        else:
            low = int(mid) + 1
        mid = (high + low ) / 2
    return -int(mid)-1
list = [1,2,3,4,5,6,7,8,9]
print(bianrySearch(list,7))