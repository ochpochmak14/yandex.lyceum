m = int(input())
can_be_cooked = set()
for i in range(m):
    meal = input()
    can_be_cooked.add(meal)
n = int(input())
cooked = set()
for i in range(n):
    count = int(input())
    for j in range(count):
        meal = input()
        cooked.add(meal)
print(*can_be_cooked.symmetric_difference(cooked), sep='\n')