from PIL import Image

alpha = float(input())

bird = Image.open("bird.png").convert("RGB")
dino = Image.open("dino.png").convert("RGB")
width, height = bird.size

result = Image.new("RGB", (width, height))
pixels_bird = bird.load()
pixels_dino = dino.load()
pixels_result = result.load()

for x in range(width):
    for y in range(height):
        r1, g1, b1 = pixels_bird[x, y]
        r2, g2, b2 = pixels_dino[x, y]
        r = int(alpha * r1 + (1 - alpha) * r2)
        g = int(alpha * g1 + (1 - alpha) * g2)
        b = int(alpha * b1 + (1 - alpha) * b2)
        pixels_result[x, y] = (r, g, b)

result.save("origin.png")
