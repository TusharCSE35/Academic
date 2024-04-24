import cv2

img1=cv2.imread("binary_pic1.png")
img2=cv2.imread("binary_pic2.png")

final1_NOT=cv2.bitwise_not(img1,mask=None)
final2_NOT=cv2.bitwise_not(img2,mask=None)
cv2.imshow('NOT1',final1_NOT)
cv2.imshow('NOT2',final2_NOT)
cv2.waitKey(0)