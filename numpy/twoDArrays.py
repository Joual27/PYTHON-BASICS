
import numpy as np

# a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
#
# b = np.array(a)
#
# # print(b.ndim, b.shape, b.size)
#
#
# print(b[0, 2], b[1][2])

X = np.array([[1, 2], [1, 3]])
Y = np.array([[2, 3], [1, 4]])


# print(X+Y, X-Y, X*Y,2*X )
Z = np.dot(X, Y)
print(Z,np.sin(Z), Z.T)


