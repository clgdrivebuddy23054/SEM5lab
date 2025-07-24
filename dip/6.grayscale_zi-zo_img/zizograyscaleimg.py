import cv2

image = cv2.imread(r"C:\Users\gioes\Downloads\WhatsApp Image 2025-06-26 at 11.18.47.jpeg",cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error:Image not found.")
else:
    # Seyt the zoom scale (1.0 = original size, > 1.0 = zoom in, < 1.0 = zoom out)
    scale = 1.5
    zoomed_image = cv2.resize(image , (0,0) , fx = scale, fy = scale)

    cv2.imshow('Original Image', image )
    cv2.imshow('Zoomed_Image', zoomed_image )

    cv2.waitKey(0)
    cv2.destroyAllWindows()
