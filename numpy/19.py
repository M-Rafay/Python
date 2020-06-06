import numpy as np
from numpy import newaxis

time = np.linspace(20, 145, 5)

data = np.sin(np.arange(20)).reshape(5,4)

print(time)
print(data)

ind = data.argmax(axis=0)
print(ind)

time_max = time[ind]


data_max = data[ind, xrange(data.shape[1])]