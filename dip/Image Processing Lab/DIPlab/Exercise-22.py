# 22. To create a program to convert the RGB color image to HSI image

import cv2
import numpy as np

def rgb_to_hsi(image):
    # Convert image to float and normalize to [0, 1]
    img = image.astype(np.float32) / 255.0
    R, G, B = img[:,:,2], img[:,:,1], img[:,:,0]  # OpenCV uses BGR

    # ----- Intensity -----
    I = (R + G + B) / 3

    # ----- Saturation -----
    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-6)) * min_rgb  # Avoid division by zero

    # ----- Hue -----
    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G)**2 + (R - B)*(G - B)) + 1e-6  # Avoid division by zero
    theta = np.arccos(num / den)

    H = np.where(B <= G, theta, 2 * np.pi - theta)
    H = H / (2 * np.pi)  # Normalize to [0, 1]

    # Stack HSI channels
    HSI = cv2.merge((H, S, I))
    return HSI

# Load RGB image
rgb_img = cv2.imread(r"C:\23054-AI-008\sem5\dip\Image Processing Lab\DIPlab\requirements\requirement.png")
# Convert to HSI
hsi_img = rgb_to_hsi(rgb_img)

# Display HSI channels separately
cv2.imshow('Hue', hsi_img[:,:,0])
cv2.imshow('Saturation', hsi_img[:,:,1])
cv2.imshow('Intensity', hsi_img[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()