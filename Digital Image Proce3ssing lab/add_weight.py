import cv2

img1=cv2.imread("pic3.jpg")
img2=cv2.imread("pic4.jpg")

imgFinal=cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow("Addition Method2",imgFinal)
cv2.waitKey(0)