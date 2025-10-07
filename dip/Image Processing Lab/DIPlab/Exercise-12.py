# 12.  To create a program to find histogram value and display histograph of a greyscale and
#  color image.

import cv2
import matplotlib.pyplot as plt

# Load color image
color_img = cv2.imread('Resources/sd/family-sd-2.jpg')

# Convert to grayscale
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

# ----- Grayscale Histogram -----
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.hist(gray_img.ravel(), bins=256, range=[0, 256], color='black')
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# ----- Color Histogram -----
colors = ('b', 'g', 'r')  # OpenCV uses BGR format
plt.figure(figsize=(6, 4))
for i, color in enumerate(colors):
    hist = cv2.calcHist([color_img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.title('Color Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()