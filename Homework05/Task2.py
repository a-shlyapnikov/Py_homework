# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""
import random


def player_move(name_player, candies, max_move):
    move = int(input(f'Игрок {name_player}, введите количество конфет, которое хотите взять: '))
    while True:
        if move > 0 and move <= max_move and move <= candies:
            print(f'Игрок {name_player} забрал {move} конфет')
            candies -= move
            print(f'Осталось {candies} конфет')
            break
        else:
            print('Введенное число конфет некорректно')
    return candies

def win_check(step, candies, name_player_1, name_player_2):
    if candies == 0:
        if step % 2:
            return name_player_1
        else:
            return name_player_2
    else: return False





def candy_game():
    name_player_1 = input('Введите имя первого игрока: ')
    name_player_2 = input('Введите имя второго игрока: ')
    candies = 50
    max_move = 28
    max_steps = candies//max_move
    win = False
    step = random.randint(0, 1)
    while not win:
        if step % 2:
            candies = player_move(name_player_1, candies, max_move)
        else:
            candies = player_move(name_player_2, candies, max_move)
        if step >= max_steps - 1:
            winner = win_check(step, candies, name_player_1, name_player_2)
            if winner:
                print(f'Выиграл {winner}')
                win = True

        step+= 1
candy_game()










