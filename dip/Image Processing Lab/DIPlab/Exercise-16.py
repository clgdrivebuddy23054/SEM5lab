# 16. To create a program to sharpen image.

import cv2
import numpy as np

# Load the input image (grayscale or color)
img = cv2.imread('Resources/sd/birds-sd-1.jpg')  # Use cv2.IMREAD_GRAYSCALE if needed

# Define a sharpening kernel (3x3)
sharpen_kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

# Apply the sharpening filter
sharpened_img = cv2.filter2D(img, -1, sharpen_kernel)

# Display original and sharpened images
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()