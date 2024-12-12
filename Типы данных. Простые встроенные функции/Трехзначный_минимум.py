n = int(input())

a = n // 100
b = n // 10 % 10 
c = n % 10 

mn = min(a, min(b, c))
mx = max(a, max(b, c))
if (a == mn and b == mx) or (b == mn and a == mx):
    th = c 
elif (a == mn and c == mx) or (c == mn and a == mx):
    th = b 
elif (c == mn and b == mx) or (c == mx and b == mn):
    th = a 

# print(mn)
# print(mx)
# print(th)

if mn == 0 and th != 0:
    print(str(th) + str(mn) + str(mx))
elif mn == 0 and th == mn:
    print(str(mx) + '0' + '0')
else:
    print(str(mn) + str(th) + str(mx))
