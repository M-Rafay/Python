import numpy as np

a= np.floor(10*np.random.random((3,4)))
print(a)

print(a.shape)
print(a.ravel())

print(a.reshape(6,2))

print(a.T)

a.resize((2,6))
print(a)