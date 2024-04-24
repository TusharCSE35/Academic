import cv2

image = cv2.imread('apple.jpg')
height, width, channels = image.shape

output = image.copy()

for y in range(height):
    for x in range(width):
        output[y][x] = image[height - y - 1][x]

cv2.imshow('Original Image', image)
cv2.imshow('Output Image', output)

cv2.waitKey(0)
cv2.destroyAllWindows()

