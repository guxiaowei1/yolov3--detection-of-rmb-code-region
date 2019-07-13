import os
from skimage import io
with open('Moneytest.txt','r') as f:
    while 1:
     line=f.readline()
     if line == '\n' or line == '':
         break
     img=io.imread('/home/xu519/gu/yolo/images/train1/'+ line[0:-1])
     io.imsave('xml/image/%s' %(line[0:-1]),img)
