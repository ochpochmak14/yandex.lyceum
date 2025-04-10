from PIL import Image


gray_value = int(input())


image = Image.open("tree.png")


tree_crop = image.crop((50, 50, 450, 450))


pixels = tree_crop.load()
for y in range(tree_crop.height):
    for x in range(tree_crop.width):
        r, g, b = pixels[x, y]
        if (r, g, b) != (255, 255, 255):
            pixels[x, y] = (gray_value, gray_value, gray_value)


shadow = tree_crop.rotate(270)
shadow = shadow.resize((shadow.width, shadow.height // 2))


image.paste(shadow, (300, 400))


image.save("shadow.png")
