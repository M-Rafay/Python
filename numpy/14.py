from numpy import newaxis
import numpy as np

a=np.floor(10*np.random.random((2,2)))
print(a)

b=np.floor(10*np.random.random((2,2)))
print(b)

print(np.column_stack((a,b)))

a= np.array([4.,2.])
b= np.array([2.,8.])
print(a[:,newaxis])