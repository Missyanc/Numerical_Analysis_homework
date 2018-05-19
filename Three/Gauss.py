import numpy as np

def guassElimin(A,b):
    '''
    高斯消去法
    :param A: 系数矩阵
    :param b: b
    :return: 方程的解向量
    '''
    n = len(b)
    for k in range(0,n-1): #上一行
        for i in range(k + 1,n): # 下一行
            if A[i,k] != 0.0: # 待消去的那一行的第一个有效数字不为0
                alpha = A[i,k] / A[k,k] # 系数
                # 一行一行开始消去
                A[i,k+1 : n] = A[i,k+1 : n] - alpha * A[k,k+1 : n]
                # 处理b
                b[i] = b[i] - alpha * b[k]
    # 从b最后一个开始计算方程的解,注意步长为-1
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(A[k,k+1 : n],b[k+1 : n])) / A[k,k]
    return b