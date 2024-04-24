import cv2

img1=cv2.imread("pic3.jpg")
img2=cv2.imread("pic4.jpg")

imgFinal=cv2.subtract(img1,img2)
cv2.imshow("Output",imgFinal)
cv2.waitKey(0)