def arithmetic_operation(op: str):
    if op == "+":
        return lambda x, y: x + y
    elif op == "-":
        return lambda x, y: x - y
    elif op == "*":
        return lambda x, y: x * y
    elif op == "/":
        return lambda x, y: x / y
