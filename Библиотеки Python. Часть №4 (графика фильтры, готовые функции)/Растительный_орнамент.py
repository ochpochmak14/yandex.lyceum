from PIL import Image, ImageOps

s = int(input().strip())
border_size = s // 10
border_color = "#208d80"

image = Image.open("ornament.png")
ornament_size = s - 2 * border_size
image = ImageOps.contain(image, (ornament_size, ornament_size))

tile = Image.new("RGB", (s, s), border_color)
tile.paste(image, (border_size, border_size))

tile.save("tile.png")
