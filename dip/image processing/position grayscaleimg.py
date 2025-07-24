import cv2
import numpy as np
image = cv2.imread(r"C:\Users\gioes\Downloads\WhatsApp Image 2025-06-26 at 11.18.47.jpeg",cv2.IMREAD_GRAYSCALE)

x_shift = 100
y_shift = 70

M = np.float32([[1,0,x_shift], [0,1,y_shift]])

shifted_image = cv2.warpAffine(image, M , (image.shape[1],image.shape[0]))

cv2.imshow('Original Image', image )
cv2.imshow('Shifted_Image', shifted_image )

cv2.waitKey(0)
cv2.destroyAllWindows()