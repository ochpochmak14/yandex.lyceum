s1 = input()
s2 = input()
cows = 0
bulls = 0

for i in range(len(s1)):
    if s1[i] in s2 and s1[i] != s2[i]:
        cows += 1 
    elif s1[i] in s2 and s1[i] == s2[i]:
        bulls += 1 
print(bulls, cows)