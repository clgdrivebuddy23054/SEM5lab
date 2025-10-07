import cv2 
image = cv2.imread(r"C:\Users\gioes\Downloads\WhatsApp Image 2025-06-26 at 11.18.47.jpeg")

if image is None:
    print("Error : Image not found.")
else:
    grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,binary_image = cv2.threshold(grey_image,127,255,cv2.THRESH_BINARY)
    print(type(image))
    print(type(binary_image))
    cv2.imshow('Binary Image',binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()