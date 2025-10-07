# 21. To create a program to obtain R, G, B values of an image.

import cv2

# Load the image in color (default is BGR)
img = cv2.imread('Resources/sd/nature-sd-1.jpg')

# Get image dimensions
height, width, channels = img.shape
print(f"Image size: {width}x{height}, Channels: {channels}")

# Access RGB values of a specific pixel (e.g., at position x=100, y=100)
(B, G, R) = img[100, 100]
print(f"Pixel at (100, 100) - R: {R}, G: {G}, B: {B}")

