import numpy as np

a = np.array([1,2,3,4])
print(a)

print("\n")

b = np.array([(1.5,2,3),(4,5,6)])
print(b)

print("\n")

a=np.zeros((3,4))
print(a)

print("\n")

a=np.zeros((3,4),dtype=np.int16)
print(a)

print("\n")

a= np.ones((2,3,4),dtype=np.int16)
print(a)

print("\n")

a=np.empty((2,3),dtype=np.int16)
print(a)
