import cv2
import numpy as np
# Load the grayscale image
image = cv2.imread(r'C:\Users\gioes\Desktop\yellow.jpg',
cv2.IMREAD_GRAYSCALE)
# Define shift values
x_shift = 100 # Shift right
y_shift = 70 # Shift down
# Create the transformation matrix for shifting
M = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
# Shift the image
shifted_image = cv2.warpAffine(image, M, (image.shape[1],
image.shape[0]))
# Display the original and shifted images
cv2.imshow('Original Image', image)
cv2.imshow('Shifted Image', shifted_image)
# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
