def simple_map(transformation, values: list) -> list:
    ans = []
    for item in values:
        ans.append(transformation(item))
    return ans