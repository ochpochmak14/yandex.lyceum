import sys 

data = list(map(str.strip, sys.stdin))
parts = list()
for item in data:
    item = [int(x.strip()) for x in item.split(";")]
    brak = list(filter(lambda x: x % 5 == 0, item))
    parts.append(len(brak))
if all(parts):
    print("FAIL")
else:
    print("OK")
