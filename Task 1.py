import numpy as np
import cv2
import math
def color (imgsize):
    cornersize = int(math.floor(imgsize/8))
    img = np.ones((imgsize,imgsize,3));
    img[:cornersize,:cornersize]=(0,0,1);
    img[:cornersize:,-cornersize:]=(0,1,0);
    img[-cornersize:,:cornersize]=(1,0,0);
    img[-cornersize:,-cornersize:]=(0,0,0);
    cv2.imshow('img',img)
    cv2.waitKey(0)
color(500);
