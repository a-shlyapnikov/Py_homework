# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def get_console_number(message):
    user_number = int(input(message))
    if 0 < user_number < 5:
        return user_number
    else:
        print('Invalid value')
        return get_console_number(message)


def find_coordinates(quater):
    print('Диапазон координат точек в указанной четверти:')
    if quater == 1:
        return print('x > 0 и y > 0')
    elif quater == 2:
        return print('x < 0 и y > 0')
    elif quater == 3:
        return print('x < 0 и y > 0')
    else:
        return print('x > 0 и y < 0')


quater = get_console_number('Введите номер четверти')
find_coordinates(quater)
