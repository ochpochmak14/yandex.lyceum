class Balance:
    def __init__(self):
        self.right_side = 0
        self.left_side = 0
        
    def add_right(self, weight):
        self.right_side += weight

    def add_left(self, weight):
        self.left_side += weight

    def result(self):
        if self.right_side > self.left_side:
            return 'R'
        elif self.right_side < self.left_side:
            return 'L'
        else:
            return '='
    