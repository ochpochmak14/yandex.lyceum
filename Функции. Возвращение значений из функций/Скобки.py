def brackets(test_string: str) -> bool:
    if test_string == "":
        return True
    stack = []
    for item in test_string:
        if item == '(':
            stack.append(item)
        elif item == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False
        