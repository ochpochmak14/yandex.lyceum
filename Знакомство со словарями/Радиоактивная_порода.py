t = input().split()
h = {t[i]: int(t[i + 1]) for i in range(0, len(t), 2)}
v = [i for i in zip(input().split(), map(float, input().split()))] 
m = float(input()) 
i = 0 
while sum([t[1] * 0.5 ** (i // h[t[0]]) for t in v]) > m:
    i += 1
print(i)
print(*[t[1] * 0.5 ** (i // h[t[0]]) for t in v])