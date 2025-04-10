from PIL import Image, ImageFilter


def motion_blur(n):
    img = Image.open("image.jpg")
    img = img.rotate(270, expand=True)
    img = img.filter(ImageFilter.GaussianBlur(n))
    img.save("res.jpg")
