def check_string(input_string):
    unique_chars = set(input_string)
    length = len(input_string)
    if len(unique_chars) < length and length >= 8:
        if (
            ("2" not in input_string)
            and ("4" not in input_string)
            and ("6" not in input_string)
            and ("8" not in input_string)
            and ("0" not in input_string)
        ):
            return input_string


def express(*input_data):
    result = []
    for current_string in filter(check_string, input_data):
        for index in range(len(input_data)):
            if input_data[index] == current_string and (index + 1) % 7 != 0:
                result.append(current_string)
                break
    return result
