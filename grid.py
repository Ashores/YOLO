import os
import glob
import cv2
import numpy as np
path='./'
cell_size=70
for file in glob.glob(path+'person.jpg'):
    name=file.split('/')[-1]
    img=cv2.imread(file)
    (w,h,_)=img.shape
    w_line=w//cell_size
    h_line=h//cell_size
    for i in range(w_line+1):
        img[i*cell_size-3:i*cell_size,:,:]=[0,0,255]
        img[0:3, :, :] = [0, 0, 255]
    for j in range(h_line+1):
        img[:,j*cell_size-3:j*cell_size,:]=[0,0,255]
        img[:, 0:3, :] = [0, 0, 255]
    cv2.imwrite('./work_dirs/'+name,img)
