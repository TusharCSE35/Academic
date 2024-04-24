import cv2

img1=cv2.imread("binary_pic1.png")
img2=cv2.imread("binary_pic2.png")

final_AND=cv2.bitwise_and(img1,img2,mask=None)
cv2.imshow('AND',final_AND)
cv2.waitKey(0)