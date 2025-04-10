from PIL import Image


img = Image.open("fruits.png")
width, height = img.size

st = input()

positions = [
    (0, 0, width // 2, height // 2),
    (width // 2, 0, width, height // 2),
    (0, height // 2, width // 2, height),
    (width // 2, height // 2, width, height),
]

parts = [img.crop(pos) for pos in positions]

new_img = Image.new("RGB", (width, height))

for i, pos in enumerate(st):
    x_offset = (i % 2) * (width // 2)
    y_offset = (i // 2) * (height // 2)
    new_img.paste(parts[int(pos) - 1], (x_offset, y_offset))

new_img.save("cycle.png")
