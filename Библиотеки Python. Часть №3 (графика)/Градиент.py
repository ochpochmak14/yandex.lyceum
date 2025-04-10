from PIL import Image


def gradient(channel):
    channel = channel.upper()
    img = Image.new("RGB", (512, 200), (0, 0, 0))
    pixels = img.load()
    red = 0
    green = 0
    blue = 0

    if channel == "R":
        for x in range(512):
            if x % 2 == 0 and x != 0:
                red += 1
            for y in range(200):
                pixels[x, y] = red, green, blue

    elif channel == "G":
        for x in range(512):
            if x % 2 == 0 and x != 0:
                green += 1
            for y in range(200):
                pixels[x, y] = red, green, blue

    elif channel == "B":
        for x in range(512):
            if x % 2 == 0 and x != 0:
                blue += 1
            for y in range(200):
                pixels[x, y] = red, green, blue

    img.save("res.png")
