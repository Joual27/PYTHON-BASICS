
import numpy as np

# b = np.array([3, 11, 5, 213, 5])
#
# b[2:] = 400,858558,744


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# select = [0 , 1, 3 , 4]
#
# arr[select] = 800
#
# print(arr.size , arr.ndim , arr.shape , arr.mean() , arr.std() , arr.max() , arr.min() , arr.sum())

#
# u = np.array([0, 1])
# v = np.array([1, 0])
#
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([20, 21, 22, 23, 24, 25])
#
# arr3 = np.array([10, 20, 30, 40, 50, 60])
# arr4 = np.array([20, 21, 22, 23, 24, 25])
#
# X = np.array([1, 2])
# Y = np.array([3, 2])
#
#
# addition = np.add(u, v)
#
# subtraction = np.subtract(arr2 , arr1)
#
# product = np.multiply(arr3, arr4)
#
# dotProduct = np.dot(X,Y)
#
# arrWithConstAddition = X + 1
#
#
# print(addition, subtraction, product, dotProduct, arrWithConstAddition)


# Math functions

#
# X = np.array([0, np.pi/2 , np.pi])
# Y = np.sin(X)
# print(Y)

x = np.linspace(0, 2*np.pi, num=100)

a = np.sin(x)

print(a)
print(x)

