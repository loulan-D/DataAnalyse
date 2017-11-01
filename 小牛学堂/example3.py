# -*- coding: utf-8 -*-
# 打印所有的水仙花数
# 题目： 打印出所有的水仙花数. "水仙花数"是指一个三位数， 其各位数字立方和等于该数本身。
# 例如： 153是一个"水仙花数"， 因为153=1的三次方＋5的三次方＋3的三次方。
# [153, 370, 371, 407]


result = []
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            n = i *100+ j *10+k
            if n == i**3+j**3+k**3:
                result.append(n)
print(result)
