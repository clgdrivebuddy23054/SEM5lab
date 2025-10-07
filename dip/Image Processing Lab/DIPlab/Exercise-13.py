# 13. To create a program to obtain histogram equalization of an image.

import cv2
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('Resources/sd/table-sd-1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_img = cv2.equalizeHist(img)

# Display original and equalized images
cv2.imshow('Original Grayscale Image', img)
cv2.imshow('Equalized Image', equalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plot histograms for comparison
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(img.ravel(), 256, (0, 256), color='gray')
plt.title('Original Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(equalized_img.ravel(), 256, (0, 256), color='black')
plt.title('Equalized Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()