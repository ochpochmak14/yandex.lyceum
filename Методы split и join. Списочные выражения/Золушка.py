substring = input()
string = input()
print(*[x for x in (string.split()) if substring in x], sep=' ')