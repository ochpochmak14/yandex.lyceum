def median(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        print((arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2)
    else:
        print(arr[len(arr) // 2])