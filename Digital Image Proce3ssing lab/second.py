import cv2

# Example usage
img = cv2.imread('Cat03.jpg',cv2.IMREAD_GRAYSCALE)

filename="Cat03_copy.jpg"
v=cv2.imwrite(filename,img)

if v==True:
    print('Image saved successfully')
else:
    print("Image save faild")      