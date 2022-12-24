# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(number):
    if number < -2:
        return fibonacci(number + 2) - fibonacci(number + 1)
    elif number == -2:
        return -1
    elif number == -1:
        return 1
    elif number == 1 or number == 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


user_number = int(input('Введите число: '))
f_list = []
for i in range(-user_number, user_number + 1):
    f_list.append(fibonacci(i))
print(f_list)
