def cleaning(*lists, **kwargs):
    result = []
    for lst in lists:
        new_lst = []
        for string in lst:
            if "max_len" in kwargs:
                string = string[:kwargs["max_len"]]

            if "big_small" in kwargs:
                if kwargs["big_small"]:
                    string = string.capitalize()
                else:
                    string = string[0].lower() + string[1:]
            if 'x_files' in kwargs:
                if "x" in string:
                    string = string.replace("x", kwargs["x_files"])
                elif "X" in string:
                    string = string.replace("X", kwargs["x_files"])
            new_lst.append(string)
        result.append(new_lst)
    return result
