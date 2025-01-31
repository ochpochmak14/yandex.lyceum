A = 0
B = 0


def voting(voice: str):
    global A, B
    if voice == "за":
        A += 1
    else:
        B += 1
    print(f"за: {A}")
    print(f"против: {B}")
    print()
    