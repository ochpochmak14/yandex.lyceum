start = int(input())
ed = int(input())
turn = int(input())

for i in range(start, ed + 1, turn):
    for j in range(start, ed + 1, turn):
        print(f"{i} + {j} = {i + j}", end='\t')
    print()
