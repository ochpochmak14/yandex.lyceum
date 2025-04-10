from PIL import Image, ImageOps

image = Image.open("portrait.png")
border_size = int(input().strip())
border_color = input().strip()

image_with_border = ImageOps.expand(image, border=border_size, fill=border_color)
image_with_border.save("border.png")
