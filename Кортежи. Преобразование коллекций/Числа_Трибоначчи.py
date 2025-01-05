n = int(input())
ls = [0] * 75 
ls[0] = 1 
ls[1] = 1 
ls[2] = 1 
for i in range(3, n):
    ls[i] = ls[i - 1] + ls[i - 2] + ls[i - 3]
    
for i in range(n):
    print(ls[i], end=' ')
  