import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Numerical_Analysis.Four.nihe as fitting
import Numerical_Analysis.Four.length as lg


if __name__ == '__main__':
    print("Import data...")
    data = pd.read_csv('E:\coursera_ML\data\ex4data.txt',sep=' ',names=['point','depth'])

    X = data["point"].values
    y = data["depth"].values
    print(X)
    print(y)

    n = 6 # 多项式次数
    p = fitting.four_fitting_func(X,y,n)

    # 画出散点图
    plt.scatter(X,y,edgecolors='r',marker='x')

    # 画出拟合曲线并和散点图在一张图上
    x = np.linspace(0,20,1000)
    y = fitting.func(p,x)
    plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2)
    plt.xticks(np.linspace(0,20,11,endpoint=True)) # 设置 x 轴的刻度

    plt.ylim(0,20)
    plt.xlabel('points')
    plt.ylabel('depth(h)')
    plt.legend()
    plt.show()

    # 求出其估计长度
    lg.compute_lenth(p,[0,20])


