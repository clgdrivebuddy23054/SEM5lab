# 18. To create a program for image compression.

import cv2

# Load the image
img = cv2.imread('Resources/sd/buffalo-sd-1.jpg')

# ----- 1. JPEG Compression (Lossy) -----
# Compression quality: 0 (worst) to 100 (best)
cv2.imwrite('compressed_jpeg_50.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])

# ----- 2. PNG Compression (Lossless) -----
# Compression level: 0 (no compression) to 9 (max compression)
cv2.imwrite('compressed_png_9.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

print("Images saved with compression.")

