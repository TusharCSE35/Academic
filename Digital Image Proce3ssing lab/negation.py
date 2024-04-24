import cv2
import numpy as np

# Load the grayscale image
image = cv2.imread('apple.jpg', cv2.IMREAD_GRAYSCALE)

# Get the maximum intensity value
max_intensity = np.max(image)

# Map the intensities to decrease linearly
output_image = max_intensity - image

# Display the original and mapped images
cv2.imshow('Original Image', image)
cv2.imshow('Mapped Image (Decreasing)', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
