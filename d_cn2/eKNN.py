#!/usr/bin/python3
#_*_ coding:utf8 _*_

import d_cn2.kNN as kNN

group, labels = kNN.createDataSet()
# print(group)
# print(labels)

result = kNN.classify0([0, 0], group, labels, 3)
print(result)