from numpy import *

# array
arr_data = random.rand(4,4)
print(arr_data)

print()

# matrix 矩阵的逆运算
randMat = mat(arr_data)
invRandMat = randMat.I
print(invRandMat)

print()

# 单位矩阵（包含误差）
myEye = randMat * invRandMat
print(myEye)

print()

# 获取误差值
print(myEye - eye(4)) # eye(4) 创建4×4的单位矩阵

print()

# N次方根
print(125 ** (1.0/3))
