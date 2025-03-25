import sys 

data = list(map(str.strip, sys.stdin))
analize = list()
for item in data:
    item = [1 if x == '0' else 0 for x in item.split()]
    analize.append(any(item))
print(any(analize))
    
    