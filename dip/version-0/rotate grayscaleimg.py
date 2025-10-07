from PIL import Image

img = Image.open(r"C:\Users\gioes\Downloads\WhatsApp Image 2025-06-26 at 11.18.47.jpeg").convert('L')

rotated_img = img.rotate(45,expand = True)

rotated_img.save('rotated_image.jpg')

img.show()
rotated_img.show()
