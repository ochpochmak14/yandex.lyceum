def bracket_check(test_string):
    if test_string == "":
        print("YES")
        return
    if test_string[0] == ')' or test_string[len(test_string) - 1] == '(':
        print("NO")
        return
    stack = []
    for item in test_string:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0:
                print("NO")
                return
            stack.pop()
    if len(stack) == 0:
        print("YES")
        return
    print("NO")
        