import sys 

data = list(map(str.strip, sys.stdin))
data = [int(x) for x in data]
if len(data) == 0:
    print(-1)
else:
    print(sum(data) / len(data))