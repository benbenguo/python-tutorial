#!/usr/bin/python3
#_*_ coding:utf8 _*_

from numpy import *
import operator
from os import listdir

"""
 生成训练数据集合标签
"""
def createDataSet():
    # 创建2维数组
    group = array([[1.0, 1.1],[1.0, 1.0],[0, 0],[0, 0.1]])
    # 创建与数组1维长度相同的列表
    labels = ['A', 'A', 'B', 'B']
    return group, labels


"""
 K 临近算法，返回距离最近的标签
"""
def classify0(inX, dataSet, labels, k):
    # 获取以为数量
    dataSetSize = dataSet.shape[0]
    # 矩阵差，tile创造矩阵 inX 行重复 dataSetSize 次，列 1 次
    # 获取向量与所有点的差值
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # 每个差值（即距离）加平方
    sqDiffMat = diffMat ** 2
    # 每个差值平方和
    # axis=1 每行数据相加，axis=0 每列数据相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 2次方根*（即平方根），获取距离
    distances = sqDistances ** 0.5
    # N * 1 矩阵，获取按列行排序后的矩阵索引
    sortedDistIndicies = distances.argsort()
    # 初始化字典
    classCount = {}
    # 循环0到k次
    for i in range(k):
        voteIlable = labels[sortedDistIndicies[i]]
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1

    # 字典转成元组列表，并按照字典的value，降序排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 返回第一个元组的第一个元素（也就是字典的key值）
    return sortedClassCount[0][0]


"""
    示例数据处理,文本数据转矩阵
"""
def file2matrix(filename):
    # 初始化分类
    love_dictionary = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}
    fr = open(filename)
    # 读取所有行
    arrayOlines = fr.readlines()
    # 获取行数
    numberOfLines = len(arrayOlines)
    # 创建Numpy矩阵, numberOfLines * 3 矩阵
    # zeros 用法见 d_numpy.start2.py
    returnMat = zeros((numberOfLines, 3))
    # 定义标签数组
    classLabelVector = []

    index = 0
    for line in arrayOlines:
        # 截取字符串前后空格
        line = line.strip()
        # 按照tab拆分字符串为字符串数组
        listFromLine = line.split('\t')
        # 矩阵初始化，每一行赋值listFromLine字符串数组
        returnMat[index, :] = listFromLine[0:3]
        # 检查字符串数组最后一个元素，是否仅由数字组成
        if (listFromLine[-1].isdigit()):
            classLabelVector.append(int(listFromLine[-1]))
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

