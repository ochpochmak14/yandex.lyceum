s = input()
print(*[s[i:len(s) - i] for i in range(len(s) // 2 + 1)], sep='\n')