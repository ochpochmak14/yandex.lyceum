from PIL import Image

desert = Image.open("desert.png")
camel = Image.open("camel.png")

x, y = map(int, input().split())
reflect = input().strip()

if reflect == "reflect":
    camel = camel.transpose(method=Image.FLIP_LEFT_RIGHT)

desert.paste(camel, (x, y))
desert.save("happy_camel.png")
    