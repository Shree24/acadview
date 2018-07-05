# QUESTION 1
import numpy as np
x=np.random.random((10,1))
z=x.mean()
print("The mean is",z)
print(np.dtype(z))
print(type(z))
print(x.shape)
# END

# QUESTION 2
x=np.random.random((20,1))
a=x.var()
print("The variance is",a)
b=x.std()
print("The standard deviation is",b)
print(np.dtype(a))
print(np.dtype(b))
print(x.shape)
print(x.dtype.name)
# END

# QUESTION 3

A=np.random.random((10,20))
B=np.random.random((20,25))
print(type(A))
print(A.dtype.name)
print(B.dtype.name)                            # in numpy there is no elementwise muliplication so dot product is used
C=np.dot(A,B)
print("The matrix muliplication is",C)
print(C.shape)
# END

# QUESTION 4
from math import exp
def f(A):
    return(1/(1+exp(-A)))
A=np.arange(10).reshape(10,1)
for i in range(1,10):
    print(f(i))


