def space_game(text):
    cnt = text.count(" ")
    if cnt % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")