from math import floor, ceil


item = input()
if len(item) - item.find('.') == 2:
    print(float(item))
    
elif int(item[-1]) >= 5:
    print(ceil(float(item) * 100) / 100)

else:
    print(floor(float(item) * 100) / 100)