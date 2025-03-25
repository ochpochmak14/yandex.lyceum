import sys

input_lines = list(map(str.strip, sys.stdin))
number_lists = []

for line in input_lines:
    numbers = [x.strip() for x in line.replace(";", " ").split() if x.strip().isdigit()]
    number_lists.append(list(map(int, numbers)))

if any(number_lists):
    max_length = max(map(len, number_lists))
    filtered_lists = [lst for lst in number_lists if len(lst) == max_length]
    result = min(map(sum, filtered_lists))
else:
    result = -1

print(result)
