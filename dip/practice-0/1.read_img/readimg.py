import cv2 
image = cv2.imread(r"C:/23054-AI-008/sem5/dip/image.jpg")

if image is None:
    print("Error : Image not found.")
else:
    cv2.imshow('Displayed Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()