ls = list()

while item := input():
    ls.append(item)
    
left = int(input())
right = int(input())

mx = 0
ans = ""

for i in range(left - 1, right):
    if len(ls[i]) > mx:
        mx = len(ls[i])
        ans = ls[i]
print(ans)