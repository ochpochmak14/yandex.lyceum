n = int(input())
for _ in range(n):   
    cubes = [int(item) for item in input().split()]

    current_answer = []

    left_pointer = 0
    right_pointer = len(cubes) - 1
    has_ans = True
    while len(current_answer) != len(cubes):
        current_max = max(cubes[left_pointer], cubes[right_pointer])
        if cubes[left_pointer] == current_max:
            left_pointer += 1
        elif cubes[right_pointer] == current_max:
            right_pointer -= 1
        if len(current_answer) == 0:
            current_answer.append(current_max)
            continue
        if current_answer[-1] < current_max:
            has_ans = False
            break
        current_answer.append(current_max)
    if has_ans:
        print(*current_answer)
    else:
        print("НЕТ")