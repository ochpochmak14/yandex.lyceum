n = int(input())

is_computer_turn = True

while n > 0:
    if is_computer_turn:
        move = n % 4 or 1
        n -= move
        print(move, n)
    else:
        while True:
            player_move = int(input())
            if 1 <= player_move <= 3:
                n -= player_move
                print(player_move, n)
                break
            print(f"Некорректный ход: {player_move}")
    is_computer_turn = not is_computer_turn
if is_computer_turn:
    print("Вы выиграли!")
else:
    print("ИИ выиграл!")
            