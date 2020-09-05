import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import cv2


num_down = 2                                     #number of downsampling steps
num_bilateral = 7                                #number of bilateral filtering steps

img_rgb = cv2.imread(".jpeg")
print(img_rgb.shape)                                #shape of the input image
img_rgb = cv2.resize(img_rgb,(800,800))           #resizing the input image for sampling   

#Downsampling by Gaussian pyramid
img_color = img_rgb
for i in range(num_down):
    img_color = cv2.pyrDown(img_color)
    
#Bilateral Filtering
for i in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color,d = 9, sigmaColor = 9, sigmaSpace = 7)

#Unsample image to original size
for i in range(num_down) :
    img_color = cv2.pyrUp(img_color)


img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray,7)

img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, blockSize = 9, C=2)
#Convert back to colour, bitwise AND with colour image
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_color, img_edge)

#display image
stack = np.hstack([img_rgb,img_cartoon])
cv2.imshow('Stack Images', stack)
cv2.waitKey(0)