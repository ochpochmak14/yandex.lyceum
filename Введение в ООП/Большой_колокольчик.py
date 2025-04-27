class BigBell:
    def __init__(self):
        self.curr = "ding"

    def sound(self):
        print(self.curr)
        if self.curr == "ding":
            self.curr = "dong"
        else:
            self.curr = "ding"