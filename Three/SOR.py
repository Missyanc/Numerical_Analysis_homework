import numpy as np

def SOR(A,b,n,womiga):
    '''
    SOR 迭代法求解方程组
    :param A: 系数矩阵
    :param b: b
    :param n: 迭代次数
    :param womiga: 松弛因子
    :return: 解向量
    '''
    m = len(b)
    jie = np.zeros(m).T
    for i in range(n): # 限制迭代次数

        for j in range(m): # 计算所有列的迭代
            sum = b[j] # 右边b
            for k in range(m): # 计算每一行的迭代
                if(j != k):
                    sum -= jie[k] * A[j][k] # 计算括号中要减去的值
            jie[j] = womiga * (sum / A[j][j])

    return jie
