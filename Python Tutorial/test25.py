import numpy as np
a = np.arange(12)
print(a)
print(a[3])
print(a[1:5])
c = a.reshape(2,-1)
print(c)
b = np.array([[100,100]])
print(np.concatenate((c,b.T), axis=1))

