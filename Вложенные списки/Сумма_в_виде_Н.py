arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
sums = []
for i in range(n - 2):
    for j in range(n - 2):
        temp = arr[i:i + 3]
        for k in range(len(temp)):
            temp[k] = temp[k][j:j + 3]
        temp_sum = 0
        for k in range(len(temp)):
            for l_ind in range(len(temp[k])):
                if l_ind == 1 and (k == 0 or k == 2):
                    continue
                else:
                    temp_sum += temp[k][l_ind]
        sums.append(temp_sum)
print(max(sums))