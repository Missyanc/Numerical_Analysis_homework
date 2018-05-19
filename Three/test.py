import Numerical_Analysis.Three.Jacobi as j
import Numerical_Analysis.Three.Guass_Seidel as gs
import Numerical_Analysis.Three.SOR as sor
import numpy as np

#课本 P55 例子
matrix1 = np.array([[10,3,1],[2,-10,3],[1,3,10]])
b1 = np.array([14,-5,14])

# J 迭代法
jie_j = j.jacobi(matrix1,b1.T,10)
print(jie_j)

# G_S 迭代法
jie_gauss_Seidel = gs.Guass_Seidel(matrix1,b1.T,10)
print(jie_gauss_Seidel)

# SOR 迭代法
jie_SOR = sor.SOR(matrix1, b1.T, 10, 1) # wimiga 为 1 即为 G_S 迭代法
print(jie_SOR)