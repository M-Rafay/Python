import numpy as np

a=np.arange(12)**2

i = np.array([1,1,3,8,5])
print(a[i])

j=np.array([[3,4],[9,7]])

print(a[j])


palette = np.array([[0,0,0],[255,0,0],[0,255,0],[0,0,255],[255,255,255]])

image = np.array([[0,1,2,0],[0,3,4,0]])

print(palette[image])