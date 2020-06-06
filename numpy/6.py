import numpy as np
from numpy import pi

a=np.ones((2,3),dtype=int)

b=np.random.random((2,3))
a *= 3
print(a)

b+=a
print(b)

print("\n")

a=np.ones(3,dtype=np.int32)

b=np.linspace(0,pi,3)
c=b.dtype.name
print(c)

d=a+b
print(d)
print(d.dtype.name)

e=np.exp(d*1j)

print(e)
print(e.dtype.name)