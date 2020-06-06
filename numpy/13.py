import numpy as np

a=np.floor(10*np.random.random((2,2)))
print(a)

b=np.floor(10*np.random.random((2,2)))
print(b)

print(np.vstack((a,b)))

print(np.hstack((a,b)))