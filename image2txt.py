import os
filetxt = open('/home/xu519/gu/yolo/labels/image.txt','w')
for _,_,file_txt in os.walk('/home/xu519/gu/yolo/labels/train1','r'):
    continue
for line in file_txt:
    filetxt.write(line.split('.')[0]+'.jpg'+'\n')