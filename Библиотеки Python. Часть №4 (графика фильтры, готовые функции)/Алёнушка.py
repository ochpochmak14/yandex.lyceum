from PIL import Image, ImageFilter

image = Image.open("picture.png")
blur_radius = int(input().strip())

reflection = image.transpose(Image.FLIP_TOP_BOTTOM)
reflection = reflection.filter(ImageFilter.GaussianBlur(blur_radius))

new_height = image.height * 2
new_image = Image.new("RGB", (image.width, new_height))

new_image.paste(image, (0, 0))
new_image.paste(reflection, (0, image.height))

new_image.save("result.png")
