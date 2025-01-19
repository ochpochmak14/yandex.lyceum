def golden_ratio(i):
    ls = [0] * (i + 1)
    ls[0] = 1
    ls[1] = 1
    for num in range(2, i + 1):
        ls[num] = ls[num - 2] + ls[num - 1]
    print(ls[i] / ls[i - 1])
    