import cv2
import numpy as np

img=cv2.imread("Tuna.jpg",cv2.IMREAD_GRAYSCALE)
img2=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
equ=cv2.equalizeHist(img2)
res=np.hstack((img2,equ))

cv2.imshow("Histogram Result",res)
cv2.waitKey(0)
cv2.destroyAllWindows()