class Rainbow:
    COLORS = ['red', 'orange', 'yellow', 'green', 'light blue', 'blue', 'violet']

    def __init__(self, number=1):
        self.colors = self.COLORS if number % 2 == 1 else list(reversed(self.COLORS))

    def next_color(self, color):
        if color in self.colors:
            index = (self.colors.index(color) + 1) % len(self.colors)
            return self.colors[index]

