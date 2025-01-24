def typification(data_list: list) -> dict:
    result = dict()
    for item in data_list:
        item_type = type(item).__name__ 
        if item_type not in result:
            result[item_type] = []
        result[item_type].append(item)
    return result
