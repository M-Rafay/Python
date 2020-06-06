import numpy as np

a = np.arange(12).reshape(3,4)
b = a > 4
print(b)

print(a[b])

a[b]=0
print(a)