class Controller:
    def __init__(self):
        self.channel = 1

    def click(self):
        self.channel = (self.channel + 1) % 6 or 1
    