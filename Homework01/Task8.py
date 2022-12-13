# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
def get_coordinate(message):
    coordinate = int(input(message))
    if coordinate != 0:
        return coordinate
    else:
        print('Введите число отличное от нуля')
        return get_coordinate(message)


def find_quater(x, y):
    if x > 0 and y > 0:
        return print('Точка находится в I четверти')
    elif x < 0 and y > 0:
        return print('Точка находится во II четверти')
    elif x < 0 and y < 0:
        return print('Точка находится в III четверти')
    else:
        return print('Точка находится в IV четверти')


x = get_coordinate('Введите абциссу(х): ')
y = get_coordinate('Введите ординату(у): ')
find_quater(x, y)
