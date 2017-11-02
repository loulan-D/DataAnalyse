# -*- coding: utf-8 -*-
# 计算指定范围内的素数
# 判断素数的方法，用这个数去除以从2开始到sqrt这个数，如果能被整除，则表明此数不是素数
# [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]（101--200）
import math

def isPrime(min,max):
    list = []
    for x in range(min,max+1):
        def isP(x):
            for i in range(2,int(math.sqrt(x))+1):
                if x%i ==0:
                    return False
            return True
        if isP(x):
            list.append(x)
    return list
print(isPrime(101,200))



