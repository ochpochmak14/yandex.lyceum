daily_food = [0, 150, 150]


def count_food(days: list) -> int:
    ans = 0
    for item in days:
        if item <= len(daily_food):
            ans += daily_food[item - 1]
    return ans
