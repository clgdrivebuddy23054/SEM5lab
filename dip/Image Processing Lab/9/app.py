from PIL import Image, ImageEnhance
image = Image.open(r"requirements\requirement.png")
enhancer = ImageEnhance.Brightness(image)
enhanced_image = enhancer.enhance(1.5)
enhanced_image = enhanced_image.convert("RGB")
enhanced_image.save("enhanced_image.jpg")
enhanced_image.show()
print("Image enhancement complete!")
