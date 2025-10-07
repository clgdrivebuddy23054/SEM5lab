# 7.  To create a program that reads a gray scale image and change the position of the
#  image.

import cv2
import numpy as np

# Load the grayscale image
img = cv2.imread('Resources/sd/war-sd-1.jpg', cv2.IMREAD_GRAYSCALE)

# Define translation values (shift right by 50 pixels, down by 30 pixels)
tx = 90  # shift along x-axis
ty = 60  # shift along y-axis

# Create the translation matrix
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the translation
translated_img = cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))

# Display the original and translated images
cv2.imshow('Original Image', img)
cv2.imshow('Translated Image', translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()