# 9. To create a program that reads a gray scale image and generates the flipped image of
#  original image.

import cv2

# Load the grayscale image
img = cv2.imread('Resources/sd/birds-sd-1.jpg', cv2.IMREAD_GRAYSCALE)

# Flip horizontally (left-right)
flip_horizontal = cv2.flip(img, 1)

# Flip vertically (top-bottom)
flip_vertical = cv2.flip(img, 0)

# Flip both horizontally and vertically
flip_both = cv2.flip(img, -1)

# Display all versions
cv2.imshow('Original Image', img)
cv2.imshow('Flipped Horizontally', flip_horizontal)
cv2.imshow('Flipped Vertically', flip_vertical)
cv2.imshow('Flipped Both', flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()