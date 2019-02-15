import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')
#x = [5,2,7]
#y = [2,18,4]

#plt.plot(x,y)
#plt.title("infogrph")
#plt.ylabel("Y axis")
#plt.xlabel("X label")
#plt.show()

x_sin = np.arange(0,3 * np.pi , 0.1)
y_sin = np.sin(x_sin)
plt.title("waveform")
plt.plot(x_sin,y_sin)
plt.show()


a=[5,8,10]
b=[12,16,6]
c=[6,9,11]
d=[6,15,7]

plt.plot(a,b,'g',label='line one',linewidth=5)
plt.plot(c,d,'c',label='line two',linewidth = 5)
plt.title("some info")
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True,color='k')
plt.show()
