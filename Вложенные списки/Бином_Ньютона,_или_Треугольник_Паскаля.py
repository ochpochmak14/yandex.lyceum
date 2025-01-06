n = int(input())
ans = list()
ans.append([1])
dp = list()
dp.append([1, 0])
for i in range(1, n):
    bf = [0] * (i + 1) 
    for j in range(0, i + 1):
        if j == 0:
            bf[j] = 1
        else:
            bf[j] = dp[i - 1][j] + dp[i - 1][j - 1]
            # print(bf[j])
        # print(bf[j])
    ans.append(bf)
    bf.append(0)
    dp.append(bf)
for item in ans:
    for j in item:
        if j != 0:
            print(j, end=' ')
    print()