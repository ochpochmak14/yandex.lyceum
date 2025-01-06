numbers = [float(item) for item in input().split()]

numbers.sort()

med = 0

if len(numbers) % 2 == 1:
    med = numbers[len(numbers) // 2]
else:
    med = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
print(sum(numbers) / len(numbers), med)