from PIL import Image, ImageDraw

hex_color = input()
digits = input()


def hex_to_rgb(hex_str: str):
    hex_str = hex_str.lstrip("#")
    return tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4))


bg_color = hex_to_rgb(hex_color)

img = Image.new("RGB", (630, 320), bg_color)
pen = ImageDraw.Draw(img)

for idx in range(6):
    pen.rectangle(
        (60 + idx * 90, 100, 120 + idx * 90, 220),
        outline=hex_to_rgb("#bfbfbf"),
        width=1,
    )
    pen.line((60 + idx * 90, 160, 120 + idx * 90, 160), hex_to_rgb("#bfbfbf"))
    pen.line((60 + idx * 90, 160, 120 + idx * 90, 100), hex_to_rgb("#bfbfbf"))
    pen.line((60 + idx * 90, 220, 120 + idx * 90, 160), hex_to_rgb("#bfbfbf"))

for index, digit in enumerate(digits):
    if digit == "0":
        pen.rectangle(
            (60 + index * 90, 100, 120 + index * 90, 220), outline=(0, 0, 0), width=3
        )
    elif digit == "1":
        pen.line((60 + index * 90, 160, 120 + index * 90, 100), (0, 0, 0), width=3)
        pen.line((120 + index * 90, 100, 120 + index * 90, 220), (0, 0, 0), width=3)
    elif digit == "2":
        pen.line((60 + index * 90, 100, 120 + index * 90, 100), (0, 0, 0), width=3)
        pen.line((120 + index * 90, 100, 120 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 220, 120 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 220, 120 + index * 90, 220), (0, 0, 0), width=3)
    elif digit == "3":
        pen.line((60 + index * 90, 100, 120 + index * 90, 100), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 160, 120 + index * 90, 100), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 160, 120 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 220, 120 + index * 90, 160), (0, 0, 0), width=3)
    elif digit == "4":
        pen.line((60 + index * 90, 100, 60 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 160, 120 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((120 + index * 90, 100, 120 + index * 90, 220), (0, 0, 0), width=3)
    elif digit == "5":
        pen.line((60 + index * 90, 100, 120 + index * 90, 100), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 100, 60 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 160, 120 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((120 + index * 90, 160, 120 + index * 90, 220), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 220, 120 + index * 90, 220), (0, 0, 0), width=3)
    elif digit == "6":
        pen.line((60 + index * 90, 160, 120 + index * 90, 100), (0, 0, 0), width=3)
        pen.rectangle(
            (60 + index * 90, 160, 120 + index * 90, 220), outline=(0, 0, 0), width=3
        )
    elif digit == "7":
        pen.line((60 + index * 90, 100, 120 + index * 90, 100), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 160, 120 + index * 90, 100), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 160, 60 + index * 90, 220), (0, 0, 0), width=3)
    elif digit == "8":
        pen.rectangle(
            (60 + index * 90, 100, 120 + index * 90, 220), outline=(0, 0, 0), width=3
        )
        pen.line((60 + index * 90, 160, 120 + index * 90, 160), (0, 0, 0), width=3)
    elif digit == "9":
        pen.line((60 + index * 90, 100, 120 + index * 90, 100), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 100, 60 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((120 + index * 90, 100, 120 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 160, 120 + index * 90, 160), (0, 0, 0), width=3)
        pen.line((60 + index * 90, 220, 120 + index * 90, 160), (0, 0, 0), width=3)

img.save("index.png")
