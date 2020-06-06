import numpy as np
from numpy import pi

a= np.arange(10)**3
print(a)

print(a[2])

print(a[2:5])
a[:6:2] = -1000
print(a)

for i in a:
    print(i**(1/3))