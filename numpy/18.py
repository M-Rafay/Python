import numpy as np

a= np.arange(12).reshape(3,4)
print(a)

i = np.array( [ [0,1],[1,2] ])

j= np.array([[2,1],[3,3]])

print(a[i,j])

print(a[i,2])

print(a[:,j])

l=[i,j]

print(a[l])

s=np.array([i,j])

print(a[tuple(s)])