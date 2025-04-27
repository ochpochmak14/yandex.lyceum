class SeaMap:
    def __init__(self):
        self.grid = [['.' for _ in range(10)] for _ in range(10)]
 
    def shoot(self, row, col, result):
        if result == 'miss':
            self.grid[row][col] = '*'
        elif result == 'hit':
            self.grid[row][col] = 'x'
        elif result == 'sink':
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < 10 and 0 <= c < 10:
                        if self.grid[r][c] == '.':
                            self.grid[r][c] = '*'
            self.grid[row][col] = 'x'
            for c in range(len(self.grid)):
                if self.grid[row][c] == 'x':
                    col = c
                    for r in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= r < 10 and 0 <= u < 10:
                                if self.grid[r][u] == '.':
                                    self.grid[r][u] = '*'
            for v in range(len(self.grid)):
                if self.grid[v][col] == 'x':
                    row = v
                    for v in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= v < 10 and 0 <= u < 10:
                                if self.grid[v][u] == '.':
                                    self.grid[v][u] = '*'
 
    def cell(self, row, col):
        return self.grid[row][col]
