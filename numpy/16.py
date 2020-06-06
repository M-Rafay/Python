import numpy as np

a=np.arange(12)
b=a
print(b is a)

b.shape=3,4
print(a.shape)

s= a[ : , 1:3]
s[:] = 10

print(a)

d=a.copy()

print(d is a)

print(d.base is a)

d[0,0] = 9999

print(d)

print(a)
