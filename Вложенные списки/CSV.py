n = int(input())
csv = list()
for i in range(n):
    item = input()
    bf = [x for x in item.split(',')]
    csv.append(bf)
q = int(input())
for i in range(q):
    query = input()
    row, column = [int(x) for x in query.split(',')]
    print(csv[row][column])