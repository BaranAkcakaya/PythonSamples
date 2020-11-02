# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:22:10 2020

@author: lenovoz
"""

import cv2

image = cv2.imread("PNG")
imageShape = image.shape
print("Resim icindeki Red değeri:",str(image.item(78,55,2)))
print("Resim icindeki Green değeri:",str(image.item(45,88,1)))
print("Resim icindeki Blue değeri:",str(image.item(145,140,0)))
rect = cv2.copyMakeBorder(image,5,5,5,5,cv2.BORDER_REPLICATE,value=(150,255,40))
#image2 = cv2.imread("11.png")
cv2.imshow("ResimDeneme",image)
cv2.imshow("ResimDeneme",rect)
cv2.waitKey(0)
#image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
#cv2.imwrite("11G.png",image)
#cv2.imwrite("112G.png",image2)
cv2.destroyAllWindows()