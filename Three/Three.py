import numpy as np
import Numerical_Analysis.Three.Gauss as guass
import Numerical_Analysis.Three.Jacobi as j
import Numerical_Analysis.Three.Guass_Seidel as gs
import Numerical_Analysis.Three.SOR as sor

def hilbert(n):
    '''
    产生新的Hilbert矩阵
    :param n: 维数
    :return: 返回矩阵
    '''

    hilbert = np.zeros((n,n))
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            hilbert[i - 1][j - 1] = float(1 / (i + j - 1))

    return hilbert

if __name__ == '__main__':

    # 产生6维的Hilbert矩阵
    hilbert_6 = hilbert(6)
    print("6维的 Hiebert 矩阵如下：")
    print(hilbert_6)

    # 产生b
    b = np.ones(6)

    # 给定解 [1,1,1,1,1,1] 求其b
    b1 = np.zeros(6)
    for i in range(6):

        b1[i] = np.dot((hilbert_6[i,:]),b.T)

    print(b1)
    # 下面设定为迭代六次
    n = 10

    # 高斯消去法
    print("\n高斯消去法得到的解向量：")
    guass_h = guass.guassElimin(hilbert_6,b1)
    print(guass_h)

    # J 迭代法
    print("\nJ 迭代法得到的解向量：")
    for i in range(1,n + 1):
        print("第 %d 次迭代结果：" %i)
        J_h = j.jacobi(hilbert_6, b1, i)
        print(J_h)

    # Gauss_Seidel 迭代法
    print("\nGuass_Seidel 迭代法得到的解向量：")
    for i in range(1,n + 1):
        print("第 %d 次迭代结果：" %i)
        gs_h = gs.Guass_Seidel(hilbert_6,b1,i)
        print(gs_h)

    # SOR 迭代法
    wimiga = 1.25 # 设置松弛因子为 1.25
    print("\nSOR 迭代法得到的解向量：")
    for i in range(1, n + 1):
        print("第 %d 次迭代结果：" % i)
        sor_h = sor.SOR(hilbert_6, b1, i, wimiga)
        print(sor_h)






