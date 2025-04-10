from PIL import Image


im = Image.open("image.jpg")
pixels = im.load()

x, y = im.size
R = 0
G = 0
B = 0
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        R += r 
        G += g 
        B += b 

s = x * y 
print(R // s, G // s, B // s)