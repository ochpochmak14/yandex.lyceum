def turbulence(left: list, right: list) -> tuple:
    def find_turbulence_start(arr: list) -> int:
        for i in range(1, len(arr) - 1):
            if (arr[i - 1] <= arr[i] > arr[i + 1]) or (arr[i - 1] >= arr[i] < arr[i + 1]):
                return i
        return -1
    left_index = find_turbulence_start(left)
    right_index = find_turbulence_start(right)  
    return left_index, right_index
