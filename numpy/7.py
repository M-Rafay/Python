import numpy as np
from numpy import pi

a = np.random.random((2,3))
print(a)

print(a.sum())

print(a.min())

print(a.max())

b = np.arange(12).reshape(3,4)
print(b)

print(b.sum(axis = 0))

print(b.sum(axis=1))

print(b.min(axis=1))

print(b.cumsum(axis=1))