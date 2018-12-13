#/usr/bin/python3
#_*_ coding:utf8 _*_

from numpy import *

# zeros 用法
# 返回来一个给定形状和类型的用0填充的数组
result = zeros(5)
print(result)

result = zeros((5,), dtype=int)
print(result)

result = zeros((2, 3))
print(result)
result[0, :] = [1, 2, 3]
print(result)