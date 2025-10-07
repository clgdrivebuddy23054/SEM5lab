# 20. To create a program to detect edges in an image using different operators.

import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('Resources/sd/birds-sd-1.jpg', cv2.IMREAD_GRAYSCALE)

# ----- 1. Sobel Operator -----
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges
sobel_combined = cv2.bitwise_or(cv2.convertScaleAbs(sobel_x), cv2.convertScaleAbs(sobel_y))

# ----- 2. Laplacian Operator -----
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian_abs = cv2.convertScaleAbs(laplacian)

# ----- 3. Canny Edge Detector -----
canny = cv2.Canny(img, threshold1=100, threshold2=200)

# ----- Display Results -----
cv2.imshow('Original Image', img)
cv2.imshow('Sobel X', cv2.convertScaleAbs(sobel_x))
cv2.imshow('Sobel Y', cv2.convertScaleAbs(sobel_y))
cv2.imshow('Sobel Combined', sobel_combined)
cv2.imshow('Laplacian', laplacian_abs)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()