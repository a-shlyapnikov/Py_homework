# Создайте программу для игры в ""Крестики-нолики"".


maps = [1, 2, 3,
        4, 5 ,6,
        7, 8 , 9]
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


def make_move(step, symbol):
    i = maps.index(step)
    maps[i] = symbol

def result():
    win = ''
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
    counter = 0
    for i in maps:
        if isinstance(i, int):
            counter +=1
    if counter == 0:
        win = 'Ничья'
    return win

game_over = False
player = True

while game_over == False:
    print_maps()
    if player == True:
        symbol = 'X'
        step = int(input('Игрок 1, ваш ход: '))
    else:
        symbol = 'O'
        step = int(input('Человек 2, ваш ход: '))
    make_move(step, symbol)
    win = result()
    if win != '':
        game_over = True
    else:
        game_over = False
    player = not(player)

print('Победил', win)