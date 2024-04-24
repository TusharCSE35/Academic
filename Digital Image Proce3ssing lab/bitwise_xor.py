import cv2

img1=cv2.imread("binary_pic1.png")
img2=cv2.imread("binary_pic2.png")

final_XOR=cv2.bitwise_xor(img1,img2,mask=None)
cv2.imshow('XOR',final_XOR)
cv2.waitKey(0)