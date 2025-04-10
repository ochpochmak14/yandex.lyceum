from PIL import Image, ImageDraw

s = int(input())
im = Image.new("RGB", (24 * s, 40 * s), "#ffffff")
draw = ImageDraw.Draw(im)
draw.polygon([int(6 * s), 11 * s, 12 * s, 3 * s, 18 * s, 11 * s], fill="#00b050")
draw.polygon([int(4 * s), 20 * s, 12 * s, 8 * s, 20 * s, 20 * s], fill="#00b050")
draw.polygon([int(2 * s), 32 * s, 12 * s, 16 * s, 22 * s, 32 * s], fill="#00b050")
draw.rectangle([int(10.5 * s), 32 * s, int(13.5 * s), 36 * s], fill="#7f6000")
im.save("fir_tree.png")
