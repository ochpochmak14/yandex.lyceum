def swap(first: list, second: list) -> None:
    first[:], second[:] = second[:], first[:]
