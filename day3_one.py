import numpy as np
a = np.array([(1,2,3),(4,5,6)])
print(a.size)
print(a.shape)
a = a.reshape(3,2)

print(a)
import time
import sys
S = range(1000)
print(sys.getsizeof(5)*len(S))
D=np.arange(1000)
print(D.size*D.itemsize)

x = np.array([(1,2,3),(3,4,5)])
y = np.array([(5,6,7),(8,9,10) , (1,2,3)])
print(x[0:,2]) #all row second column
z=np.linspace(0,1,4)
print(z)

print(np.linspace(0,1,3))

print(x-y)
print(np.dot(x,y))


print(np.identity(3))