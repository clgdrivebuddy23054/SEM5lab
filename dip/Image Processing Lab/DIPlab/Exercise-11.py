# 11. To create a program that reads a gray scale image and blur the image.

import cv2

# Load the grayscale image
img = cv2.imread('Resources/sd/people-sd-1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply a blur using a 5x5 kernel
blurred_img = cv2.blur(img, (5, 5))

# blurred_img = cv2.GaussianBlur(img, (5, 5), sigmaX=0)

# Display original and blurred images
cv2.imshow('Original Grayscale Image', img)
cv2.imshow('Blurred Image', blurred_img)

cv2.waitKey(0)
cv2.destroyAllWindows()