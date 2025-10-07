import cv2 
image = cv2.imread(r"C:\Users\gioes\Downloads\WhatsApp Image 2025-06-26 at 11.18.47.jpeg")

if image is None:
    print("Error : Image not found.")
else:
    cv2.imshow('Displayed Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
