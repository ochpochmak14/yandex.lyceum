current_weather = input()
if current_weather == 'ясно':
    yasno = 1.0
    pasmurno = 0.0
else:
    yasno = 0.0
    pasmurno = 1.0
p = float(input())
q = float(input())
count = int(input())
for _ in range(count):
    new_yasno = max(yasno * p, pasmurno * (1 - q))
    new_pasmurno = max(pasmurno * q, yasno * (1 - p))
    yasno, pasmurno = new_yasno, new_pasmurno
if yasno > pasmurno:
    print("ясно")
    print(yasno)
elif pasmurno > yasno:
    print("пасмурно")
    print(pasmurno)
else:
    print("равновероятно")
    print(yasno)