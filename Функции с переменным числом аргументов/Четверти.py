def quarters(*coordinates: tuple) -> dict:
    result = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}
    for x_coord, y_coord in coordinates:
        if not x_coord or not y_coord:
            continue
        elif x_coord > 0 and y_coord > 0:
            result['I'] += 1
        elif x_coord < 0 and y_coord > 0:
            result['II'] += 1
        elif x_coord < 0 and y_coord < 0:
            result['III'] += 1
        elif x_coord > 0 and y_coord < 0:
            result['IV'] += 1
    return result
