def print_statistics(arr):
    if len(arr) == 0:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
    else:
        print(len(arr))
        arr = sorted(arr)
        print(sum(arr) / len(arr))
        print(min(arr))
        print(max(arr))
        if len(arr) % 2 == 0:
            print((arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2)
        else:
            print(arr[len(arr) // 2])
