from PIL import Image, ImageDraw


def board(cells, cell_size):
    canvas = Image.new("RGB", (cells * cell_size, cells * cell_size), (255, 255, 255))
    painter = ImageDraw.Draw(canvas)

    for row in range(cells):
        for col in range(cells):
            if (row + col) % 2 == 0:
                painter.rectangle(
                    (
                        (row * cell_size, col * cell_size),
                        ((row + 1) * cell_size - 1, (col + 1) * cell_size - 1),
                    ),
                    0,
                )

    canvas.save("res.png")
