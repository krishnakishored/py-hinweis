'''
Matrix addition
Matrix subtraction
Matrix multiplication
Scalar product
Cross product
and lots of other operations on matrices
'''
import numpy as np
import math

x = np.array([1,5,2])
y = np.array([7,4,1])

print(x+y)
print(x*y)
print(x-y)
print(x%y)

x = np.array([3,2])
y = np.array([5,1])
z = x + y
print(z)#vector addition

'''
the dot product is an algebraic operation that takes two coordinate vectors of
equal size and returns a single number. The result is calculated by multiplying
corresponding entries and adding up those products.
a.b = |a| |b| cos(a,b)
'''

x = np.array([1,2,3])
y = np.array([-7,8,9])
print(np.dot(x,y))

dot = np.dot(x,y)
x_modulus = np.sqrt((x*x).sum())
y_modulus = np.sqrt((y*y).sum())
cos_angle = dot / x_modulus / y_modulus # cosine of angle between x and y
angle = np.arccos(cos_angle)
# print("angle: %f, cos_angle: %f" %(angle, cos_angle))
# print("x_modulus: %f, y_modulus: %f" % (x_modulus,y_modulus))
print("angle:{}, cos_angle: {}".format(angle, cos_angle))

print("x_modulus:{}, y_modulus: {}".format(x_modulus,y_modulus))

##################### Matrix Class ######################

'''
The matrix objects are a subclass of the numpy arrays (ndarray).
The matrix objects inherit all the attributes and methods of ndarry.
Another difference is that numpy matrices are strictly 2-dimensional,
while numpy arrays can be of any dimension, i.e. they are n-dimensional
'''

x = np.matrix( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)) )
print(type(x*y)) #<class 'numpy.matrixlib.defmatrix.matrix'>

#matrix product
'''
If we want to perform matrix multiplication with two numpy arrays (ndarray),
we have to use the dot product:

'''
x = np.array( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)) )
print(np.dot(x,y))
print(np.mat(x) * np.mat(y))# cast them to matrix objects

#example
NumPersons = np.array([[100,175,210],[90,160,150],[200,50,100],[120,0,310]])
Price_per_100_g = np.array([2.98,3.90,1.99])
Price_in_Cent = np.dot(NumPersons,Price_per_100_g)
Price_in_Euro = Price_in_Cent / np.array([100,100,100,100])
print(Price_in_Euro)


#Cross product
'''
The cross product or vector product is a binary operation on two vectors in
three-dimensional space. The result is a vector which is perpendicular to
the vectors being multiplied and normal to the plane containing them.
 a*b = |a||b|sin(a,b) |n| -- n is unit vector
'''

x = np.array([0,0,1])
y = np.array([0,1,0])

np.cross(x,y)
print("x:{}".format(x))
print("y:{}".format(y))
print("np.cross(x,y) {}".format(np.cross(x,y)))

print("np.cross(y,x) {}".format(np.cross(y,x)))
