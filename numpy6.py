import numpy as np 

a = np.ones([3,3])
print("Origional Matrix = \n", a)
a = np.pad(a, pad_width=1, mode='constant', constant_values=0)
print("\n",a)