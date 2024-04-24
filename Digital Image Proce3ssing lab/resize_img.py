import cv2
import numpy as np

image = cv2.imread('apple.jpg', cv2.IMREAD_GRAYSCALE)
height, width = image.shape
output_image = np.zeros((height, width), dtype=np.uint8)

max_intensity = np.max(image)
for y in range(height):
    for x in range(width):
        output_image[y, x] = int(max_intensity - image[y, x] * (max_intensity / 255))


cv2.imshow('Original Image', image)
cv2.imshow('Mapped Image Decreasing', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
