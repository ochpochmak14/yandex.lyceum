n = int(input())
res = 0
for num in range(1, n + 1):
    my_sm = 0
    for degree in range(0, num + 1):
        if degree % 2 == num % 2:
            my_sm += degree
    res += num ** my_sm
print(res)