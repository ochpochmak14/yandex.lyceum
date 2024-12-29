n = int(input())
prev1 = 1 
prev2 = 1
number = 2
while True:
    curr = prev1 + prev2
    prev1, prev2 = prev2, curr
    number += 1 
    if n == curr:
        print(number)
        break
    if n < curr:
        print("НЕТ")
        break
    