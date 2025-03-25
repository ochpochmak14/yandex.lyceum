import sys 

data = list(map(str.strip, sys.stdin))
cnt = 0
ans = "EVERGREEN TOMATOES"
for item in data:
    item = item.split()
    item2 = list(filter(lambda x: '0' in str(x), item))
    if len(item2) > len(item) - len(item2):
        ans = "ALUMINUM CUCUMBERS"
        break 
    
print(ans)

    