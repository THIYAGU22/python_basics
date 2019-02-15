import numpy as np
#a = []
a = np.array([1+2j,2+5j,87])
print("complex values checking",np.iscomplex(a))
print("integer values checking",np.isreal(a))


for x in range(len(a)):
    if np.isreal(a[x]):
        print("it is real")
    elif np.iscomplex(a[x]):
        print("it is complex")

    elif a[x]<a[x+1]:
        print("it is greater")