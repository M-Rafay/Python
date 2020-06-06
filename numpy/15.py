import numpy as np

a=np.arange(12)
b=a
print(b is a)

b.shape=3,4
print(a.shape)

def f(x):
    print(id(x))

print(id(a))

f(a)

c= a.view()
print(c is a)

print(c.base is a)

print(c)

print(c.flags.owndata)

c.shape=2,6
print(a.shape)

print(c)
c[0,4]= 1234
print(a)