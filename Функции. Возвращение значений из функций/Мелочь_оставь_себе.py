def take_large_banknotes(banknotes: list[int]) -> list[int]:
    ans = [x for x in banknotes if x > 10]
    return ans