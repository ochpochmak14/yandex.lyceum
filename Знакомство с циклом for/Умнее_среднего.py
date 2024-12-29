n = int(input())
static = 0
num = int(input())
print(0)
sm = num
k = 1
for i in range(n - 1):
    static = sm / k 
    iq = int(input())
    if iq == static:
        print(0)
    elif iq < static:
        print('<')
    else:
        print('>')
        
    sm += iq
    k += 1
