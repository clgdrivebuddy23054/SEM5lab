# 15. To create a program for image enhancement.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (color)
img = cv2.imread('Resources/sd/nature-sd-1.jpg')

# ----- 1. Brightness & Contrast Adjustment -----
brightness = 30   # increase brightness
contrast = 1.5    # scale contrast
enhanced_bc = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)

# ----- 2. Histogram Equalization (for grayscale) -----
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)

# ----- 3. Sharpening Filter -----
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, kernel_sharpen)

# ----- 4. Denoising -----
denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

# ----- Display Results -----
titles = ['Original', 'Brightness & Contrast', 'Equalized (Gray)', 'Sharpened', 'Denoised']
images = [img, enhanced_bc, equalized, sharpened, denoised]

plt.figure(figsize=(15, 8))
for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    if titles[i] == 'Equalized (Gray)':
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()