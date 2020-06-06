filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


import numpy as np
a= np.array([2,3,4])
print(a.dtype)