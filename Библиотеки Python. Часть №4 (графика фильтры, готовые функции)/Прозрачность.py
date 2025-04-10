from PIL import Image


def transparency(ﬁlename1, ﬁlename2):
    img_a = Image.open(ﬁlename1)
    img_b = Image.open(ﬁlename2)

    pixels_a = img_a.load()
    pixels_b = img_b.load()

    width, height = img_a.size

    for i in range(width):
        for j in range(height):
            red_a, green_a, blue_a = pixels_a[i, j]
            red_b, green_b, blue_b = pixels_b[i, j]

            blended_pixel = (
                int(0.5 * red_a + 0.5 * red_b),
                int(0.5 * green_a + 0.5 * green_b),
                int(0.5 * blue_a + 0.5 * blue_b),
            )

            pixels_a[i, j] = blended_pixel

    img_a.save("res.jpg")
