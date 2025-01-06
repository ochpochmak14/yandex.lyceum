r = [int(x) for x in input().split()]
result = []
for a in r:
    if a == 0:
        d = {'digits': 1, 'units': 0, 'zeros': 1}
    else:
        u, z = 0, 0
        temp = a
        while temp > 0:
            if temp % 2 == 0:
                z += 1
            else:
                u += 1
            temp = temp // 2
        d = {'digits': u + z, 'units': u, 'zeros': z}
    result.append(d)
print(result)
