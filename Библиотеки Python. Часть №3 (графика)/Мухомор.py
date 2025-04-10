from PIL import Image, ImageDraw

bg_r, bg_g, bg_b = map(int, input().split())
cell_size = int(input())

width, height = 20 * cell_size, 22 * cell_size

cap_color = (192, 0, 0)
stem_color = (255, 250, 235)
dot_color = (255, 255, 255)
grass_color = (146, 208, 80)

image = Image.new("RGB", (width, height), (bg_r, bg_g, bg_b))
draw = ImageDraw.Draw(image)
stem_x1 = 7 * cell_size
stem_x2 = 13 * cell_size
stem_y1 = 7 * cell_size
stem_y2 = 20 * cell_size
draw.ellipse([stem_x1, stem_y1, stem_x2, stem_y2], fill=stem_color)

draw.rectangle(
    [3 * cell_size, 19 * cell_size, 17 * cell_size, 20 * cell_size], fill=grass_color
)


cap_x1 = 4 * cell_size
cap_x2 = 17 * cell_size
cap_y1 = 4 * cell_size
cap_y2 = 17 * cell_size
draw.arc(
    [cap_x1, cap_y1, cap_x2, cap_y2], 180, 360, fill=cap_color, width=width * height
)

dot_radius = cell_size // 2
dots = [(6, 8), (10, 7), (10, 5), (11, 6), (14, 8), (15, 9)]
draw.ellipse(
    [(6 * cell_size, 8 * cell_size), (7 * cell_size, 9 * cell_size)], fill=dot_color
)
draw.ellipse(
    [10 * cell_size, 5 * cell_size, 11 * cell_size, 6 * cell_size], fill=dot_color
)
draw.ellipse(
    [14 * cell_size, 8 * cell_size, 15 * cell_size, 9 * cell_size], fill=dot_color
)

image.save("mushroom.png")
