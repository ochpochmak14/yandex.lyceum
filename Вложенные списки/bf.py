s = [0 for i in range(30001)]
pos = 0
a = input()
i = 0
while i < len(a):
    if a[i] == ">":
        pos = pos + 1
    elif a[i] == "<":
        pos = pos - 1
    elif a[i] == ".":
        print(s[pos])
    elif a[i] == "+":
        s[pos] = s[pos] + 1
        if s[pos] > 255:
            s[pos] = 0
    elif a[i] == "-":
        s[pos] = s[pos] - 1
        if s[pos] < 0:
            s[pos] = 255
    elif a[i] == "[":
        if s[pos] == 0:
            j = i + 1
            c = 1
            while True:
                if a[j] == "[":
                    c += 1
                if a[j] == "]":
                    c -= 1
                if c == 0:
                    i = j
                    break
                j += 1
    elif a[i] == "]":
        c = -1
        j = i - 1
        while True:
            if a[j] == "]":
                c -= 1
            if a[j] == "[":
                c += 1
            if c == 0:
                i = j - 1
                break
            j -= 1

    i += 1
