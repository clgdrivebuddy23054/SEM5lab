# 17. To create a program for Image Restoration.

import cv2
import numpy as np

# Load the degraded image (grayscale or color)
img = cv2.imread('Resources/sd/buffalo-sd-1.jpg')

# ----- 1. Denoising (Non-Local Means) -----
denoised = cv2.fastNlMeansDenoisingColored(img, None, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21)

# ----- 2. Deblurring (Using Gaussian Blur + Sharpening) -----
blurred = cv2.GaussianBlur(img, (3, 3), 0)
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
deblurred = cv2.filter2D(blurred, -1, sharpen_kernel)

# ----- 3. Inpainting (Restoring damaged regions using a mask) -----
# Create a synthetic mask (white = damaged area)
mask = np.zeros(img.shape[:2], dtype=np.uint8)
mask[50:150, 50:150] = 255  # simulate a damaged patch

# Apply inpainting
inpainted = cv2.inpaint(img, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# ----- Display Results -----
cv2.imshow('Original Image', img)
cv2.imshow('Denoised Image', denoised)
cv2.imshow('Deblurred Image', deblurred)
cv2.imshow('Inpainted Image', inpainted)
cv2.waitKey(0)
cv2.destroyAllWindows()