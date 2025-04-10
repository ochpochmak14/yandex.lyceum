from PIL import Image, ImageDraw

s = int(input())
width, height = 70 * s, 70 * s

bg_color = (255, 255, 255)
circle_color = (0, 112, 192)
upper_snake_color = (255, 255, 255)
lower_snake_color = (255, 192, 0)

image = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(image)


circle_bbox = [0 * s, 0 * s, 70 * s, 70 * s]
draw.ellipse(circle_bbox, fill=circle_color)


draw.polygon(
    [
        26 * s,
        12 * s,
        45 * s,
        12 * s,
        45 * s,
        34 * s,
        24 * s,
        34 * s,
        24 * s,
        44 * s,
        14 * s,
        44 * s,
        14 * s,
        24 * s,
        35 * s,
        24 * s,
        35 * s,
        22 * s,
        26 * s,
        22 * s,
    ],
    fill=upper_snake_color,
)
draw.ellipse([28 * s, 14 * s, 34 * s, 20 * s], fill=circle_color)


draw.polygon(
    [
        47 * s,
        26 * s,
        57 * s,
        26 * s,
        57 * s,
        46 * s,
        35 * s,
        46 * s,
        35 * s,
        48 * s,
        45 * s,
        48 * s,
        45 * s,
        58 * s,
        26 * s,
        58 * s,
        26 * s,
        36 * s,
        47 * s,
        36 * s,
    ],
    fill=lower_snake_color,
)
draw.ellipse([37 * s, 50 * s, 43 * s, 56 * s], fill=circle_color)

image.save("python_logo.png")
