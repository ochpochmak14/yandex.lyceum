def average(values: list) -> float:
    if len(values) == 0:
        return 0
    return sum(values) / len(values)