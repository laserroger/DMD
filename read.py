from __future__ import division
import numpy as np
import sys

if len(sys.argv) == 1:
 name = 'image.data'
else:
 name = 'image' + sys.argv[1] + '.data'

width = 1024
height = 768
stream = open(name,'rgb')

stream.seek(0)
fwidth = (width + 31) //32 * 32
fheight = (height + 15) // 16 * 16

image = np.fromfile(stream,dtype = np.uint8).\
        reshape((fheight, fwidth, 3))[:height, :width, :]

#print image

#image = image.astype(np.float, copy=False)
#image = image/255.

grayscale = [[0 for i in range(1024)] for j in range (768)]
for d1 in range(768):
 for d2 in range(1024):
  grayscale[d1][d2] = 0.2126*image[d1][d2][0]**2.2 + 0.7152*image[d1][d2][1]**2.2 + 0.0722*image[d1][d2][0]**2.2

#file = open("newfile.txt", "w")
#file.write(grayscale)
#file.close()

print np.amax(grayscale)

a = np.array(grayscale)
i,j = np.unravel_index(a.argmax(), a.shape)
print i, j

sum = 0
for d1 in range(i-5, i+5):
 for d2 in range(j-5, j+5):
  sum = sum + grayscale[d1][d2]

print sum