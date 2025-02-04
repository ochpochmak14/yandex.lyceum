def transpose(matrix):
    matrix[:] = [list(row) for row in zip(*matrix)]
