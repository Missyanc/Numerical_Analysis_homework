import numpy as np
from scipy.optimize import leastsq

def four_fitting_func(x,y,n):
    '''
    用最小二乘法拟合
    :param x: 拟合的自变量值
    :param y: 拟合的函数值
    :param n: 拟合的多项式次数
    :return: 返回多项式的系数
    '''
    p0 = np.zeros(n + 1) # 因为 n 次多项式其实是有 n+1 个待定系数，初始全为0
    Para = leastsq(error, p0, args=(x, y)) # 用 leastsp 方法拟合，其实是最小二乘法
    print(Para)
    p = np.array(Para[0])
    print("%d次拟合结果如下：" %n)
    print(p)
    return p

def func(p,x):
    '''
    产生拟合的函数func
    :param p: 多项式系数
    :param x: x
    :return: 多项式
    '''

    #不知道为什么下面的代码就是有问题，有时间再研究
    temp_p = np.array(p) # 参数列表
    # print(temp_p)
    # # 多项式形式
    # fitting_func = 0.0
    #
    # for i in range(len(temp_p)):
    #     print(i)
    #     fitting_func += temp_p[i] * (x ** (len(temp_p - 1) - i))
    # print(fitting_func)

    # 七次拟合
    #fitting_func = temp_p[0] * (x ** 7) + temp_p[1] * (x ** 6) + temp_p[2] * (x ** 5) + temp_p[3] * (x ** 4) \
    #              + temp_p[4] * (x ** 3) + temp_p[5] * (x**2) + temp_p[6] * x + temp_p[7]

    # 六次拟合
    fitting_func = temp_p[0] * (x ** 6) + temp_p[1] * (x ** 5) + temp_p[2] * (x ** 4) \
                  + temp_p[3] * (x ** 3) + temp_p[4] * (x ** 2) + temp_p[5] * x + temp_p[6]

    # 五次拟合
    #fitting_func = temp_p[0] * (x ** 5) + temp_p[1] * (x ** 4) + temp_p[2] * (x ** 3) + temp_p[3] * (x ** 2) + temp_p[4] * x + temp_p[5]

    # 四次拟合
    #fitting_func = temp_p[0] * (x ** 4) + temp_p[1] * (x ** 3) + temp_p[2] * (x ** 2) + temp_p[3] * x + temp_p[4]

    # 三次拟合
    #fitting_func = temp_p[0] * (x ** 3) + temp_p[1] * (x ** 2) + temp_p[2] * x + temp_p[3]
    return fitting_func

def error(p,x,y):
    '''
    拟合的残差
    :param p:
    :param x:
    :param y:
    :param s:
    :return:
    '''
    return func(p,x) - y # x、y都是列表，故返回值也是个列表








