class OddEvenSeparator:
    def __init__(self):
        self.odd1 = []
        self.even1 = []

    def add_number(self, number):
        if number % 2 == 0:
            self.even1.append(number)
        else:
            self.odd1.append(number)

    def even(self):
        return self.even1

    def odd(self):
        return self.odd1