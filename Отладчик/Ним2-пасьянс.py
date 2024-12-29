first = int(input())
second = int(input())
while True:
    if first == 0 and second == 0:
        break
    a = int(input())
    b = int(input())
    if a == 1:
        first -= b 
        
    elif a == 2:
        second -= b 
    
    print(first, second)
