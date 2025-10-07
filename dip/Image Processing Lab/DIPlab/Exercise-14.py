# 14. To create a program to implement smoothing or averaging filter in spatial domain.

import cv2
import numpy as np

# Load the grayscale image
img = cv2.imread('Resources/sd/family-sd-2.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel size (e.g., 5x5)
kernel_size = (5, 5)

# Apply the averaging filter (mean filter)
smoothed_img = cv2.blur(img, kernel_size)

# Display the original and smoothed images
cv2.imshow('Original Grayscale Image', img)
cv2.imshow('Smoothed Image (Averaging Filter)', smoothed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()