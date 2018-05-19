import sympy as sy
from sympy import *


def func_compute(func):
    '''
    返回求解弧长的表达式
    :param func: 原函数
    :return: 一个积分
    '''
    f, g = symbols('f g', cls=Function)
    x, y, a, b = symbols('x y a b')
    func = diff(f(x))
    # pprint(f(x))
    pprint(integrate(sqrt(1 + func ** 2), (x, a, b)))


def compute_lenth(p,interval):
    '''
    计算多项式函数的弧长
    :param p: 多项式系数的 narray
    :param interval: 区间,传入一个 narray,包含上下限
    :return: 长度
    '''
    x = sy.symbols('x')
    n = len(p) # 有多少个系数

    # p_1 = np.zeros(n)
    # 产生多项式函数
    func = 0
    for i in range(n):
        #p_1[i] = sy.evaluate(p[i])
        func += (p[i] * (x ** (n-1-i)))

    print('\n拟合得到的多项式函数为：')
    sy.pprint(func)

    # 用高数求弧长公式求弧长
    print('\n用以下公式求弧长：')
    func_compute(func)

    # 对其求导
    print('\n先对其求导，其导数为：')
    func1 = sy.diff(func,x)
    sy.pprint(func1)
    func2 = sy.sqrt(1 + func1**2)

    #sy.pprint(func2)
    # func3 = sy.integrate(func2,x)
    # sy.pprint(func3)
    a = sy.integrate(func2,(x,interval[0],interval[1])) # 积分函数
    b = sy.nfloat(a,5) # 积分值，保留五位有效数字

    print('\n这是求解该长度定积分的函数表达式：')
    sy.pprint(a)
    print('\n估计长度为：')
    sy.pprint(b)




