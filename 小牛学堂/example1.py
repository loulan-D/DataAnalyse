# -*- coding: utf-8 -*-

# 有限排列问题
# 有四个数字： 1、 2、 3、 4， 能组成多少个互不相同且无重复数字的三位数？ 各是多少？
# demo1
# list = ["%d%d%d" % (x, y, z) for x in range(1, 5) for y in range(1, 5) for z in range(1, 5) if( x != y ) and (x != z) and(y != z) ]
# print(list)
# print(len(list))

# demo2
# list = ["{}{}{}".format(x,y,z) for x in range(1,5) for y in range(1,5) for z in range(1,5) if(x!=y) and (x!=z)and (y!=z)]
# print(list,len(list))

# demo3
# list = []
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if(x!=y)and(x!=z)and(y!=z):
#                 list.append((x,y,z))
# print(list,len(list))

# demo4
list = []
for x in range(1,5):
    for y in range(1,5):
        if(x!=y):
            for z in range(1,5):
                if(x!=z)and(y!=z):
                    list.append((x,y,z))
print(list,len(list))