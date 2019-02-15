import os
os.chdir('C:\Users\Administrator\Desktop')

from scipy import misc
f = misc.face()
misc.imsave('hero.jfif',f)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()

f = misc.imread('hero.jfif')
print(type(f))

print(f.shape)

print(f.dtype)

f.tofile('hero.raw')

import np
fromraw=np.fromfile('hero.raw',dtype=np.uint8)
fromraw.shape

fromraw.shape=(768, 1024, 3)

memmap = np.memmap('hero.raw', dtype=np.uint8, shape=(768, 1024, 3))

for i in range(7):
    im=np.random.randint(0,256,10000).reshape((100,100))
    misc.imsave('random_%02d.png'%i,im)

from glob import glob
filelist=glob('random*.png')
filelist.sort()

f1=misc.face(gray=True)
plt.imshow(f1,cmap=plt.cm.gray)

plt.imshow(f1,cmap=plt.cm.gray,vmin=30,vmax=200)
plt.axis('off') #This removes axes and ticks
plt.contour(f1,[50,200])

plt.imshow(f1[320:340, 510:530], cmap=plt.cm.gray, interpolation='bilinear')