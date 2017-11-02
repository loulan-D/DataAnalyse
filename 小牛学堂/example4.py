# -*- coding: utf-8 -*-
# 斐波那契数列 0 1 1 2 3 5 8 13 21 34...
# 在数学中，其以递归的形式定义：
"""
f0 = 0
f1 = 1
fn = f(n-1)+f(n-2)
"""
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1)+f(n-2)
print(f(10))
