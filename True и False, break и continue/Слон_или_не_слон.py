hobot = 0
hvost = 0
nogi = 0
uxi = 0
eyes = 0
mouth = 0
while True:
    count = int(input())
    body_part = input()
    eyes2 = eyes // 2
    uxi2 = uxi // 2
    nogi2 = nogi // 4
    if min(hobot, min(hvost, min(nogi2, min(uxi2, min(eyes2, mouth))))) > 0:
        print('Есть слон!')
        print(min(hobot, min(hvost, min(nogi2, min(uxi2, min(eyes2, mouth))))))
        break
    if body_part == 'ОБЕД':
        eyes //= 2
        uxi //= 2
        nogi //= 4
        if min(hobot, min(hvost, min(nogi, min(uxi, min(eyes, mouth))))) > 0:
            print('Есть слон!')
            print(min(hobot, min(hvost, min(nogi, min(uxi, min(eyes, mouth))))))
        else:
            print('Какие-то слоны нецелые. Пошли обедать.')
        break
    
    if body_part == 'нога':
        nogi += count 
    elif body_part == 'ухо':
        uxi += count 
    elif body_part == 'глаз':
        eyes += count 
    elif body_part == 'рот':
        mouth += count 
    elif body_part == 'хобот':
        hobot += count 
    elif body_part == 'хвост':
        hvost += count 
        