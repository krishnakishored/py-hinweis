# https://www.python-course.eu/numpy_numerical_operations_on_numpy_arrays.php

import numpy as np

def test_numerical_operators():
    lst = [2, 3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9]
    v = np.array(lst)
    v = v + 2 # adding scalars to arrays
    print(v)
    print(v * 2.2)
    print(v - 1.38)
    print(v ** 2) # exponentiation 
    print(v ** 1.5)

    # to do scalar operations on lists
    lst = [2,3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9]
    res = [ val + 2 for val in lst]
    print(res)


#Arithmetic Operations with two Arrays
def test_arithmetic_operations():
    A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
    B = np.ones((3,3))
    print("Adding to arrays: ")
    print(A + B)
    print("\nMultiplying two arrays: ")
    print(A * (B + 1)) # Not Matrix Multiplication: The elements are solely component-wise multiplied 

    print("\nMatrix multiplication: ")
    print(np.dot(A,B))


def test_dot_product():
    # both arguments are scalars or one-dimensional array:
    print(np.dot(3, 4))
    x = np.array([3])
    y = np.array([4])
    print(x.ndim)
    print(np.dot(x, y))
    x = np.array([3, -2])
    y = np.array([-4, 1])
    print(np.dot(x, y))

    print("\ntwo-dimensional use case: ")
    A = np.array([ [1, 2, 3], 
               [3, 2, 1] ])
    B = np.array([ [2, 3, 4, -2], 
               [1, -1, 2, 3],
               [1, 2, 3, 0] ])
    # es muss gelten:
    print(A.shape[-1] == B.shape[-2], A.shape[1]) # True 3
    print(np.dot(A, B))


    # Matrices vs. Two-Dimensional Arrays
    print("\nTwo-Dimensional Arrays:" )
    A = np.array([ [1, 2, 3], [2, 2, 2], [3, 3, 3] ])
    B = np.array([ [3, 2, 1], [1, 2, 3], [-1, -2, -3] ])
    R = A * B
    print(R)
    print("\nMatrices:" )
    MA = np.mat(A)
    MB = np.mat(B)
    R = MA * MB
    print(R)

    print("\nComparison Operators:" )
    A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
    B = np.array([ [11, 102, 13], [201, 22, 203], [31, 32, 303] ])
    print(A == B)
    print(np.array_equal(A, B))
    print(np.array_equal(A, A))


    print("\nLogical Operators:" )
    a = np.array([ [True, True], [False, False]])
    b = np.array([ [True, False], [True, False]])
    print(np.logical_or(a, b))
    print(np.logical_and(a, b))



        
# ToDo: three dimensional , broadcasting


if __name__ == "__main__":
    # test_numerical_operators()
    # test_arithmetic_operations()
    test_dot_product()