import numpy as np

def jacobi(A,b,n):
    '''
    Jacobi迭代法求解方程组
    :param A: 系数矩阵
    :param b: b
    :param n: 迭代次数
    :return: 解向量
    '''
    m = len(b) # 解的个数
    jie = np.zeros(m).T
    for i in range(n): # 限制迭代次数

        # 用一个中间向量保存解向量，让每次迭代都是没有更新的解向量
        # 若没有 copy 或用 temp_jie = jie 的迭代都是更新的迭代
        # 解释：temp_jie = jie 的 temp_jie 只是指向 jie 的一个指针，每次改变 emp_jie 其实都是改变 jie
        temp_jie = jie.copy()

        for j in range(m): # 计算所有列的迭代
            sum = b[j] # 右边b

            for k in range(m): # 计算每一行的迭代
                #print(temp_jie[k])
                if(j != k):
                    sum -= temp_jie[k] * A[j][k] # 计算括号中要减去的值
            jie[j] = sum / A[j][j]

    return jie
