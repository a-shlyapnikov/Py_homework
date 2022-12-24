# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

n = int(input('Введите количество элементов в списке: '))
list1 = []
list2 = []

for i in range(n):
    list1.append(random.randint(0, 9))
for i in range(len(list1)):
    while i < len(list1) /2 and n > len(list1) / 2:
        n = n - 1
        list2.append(list1[i] * list1[n])
        i += 1

print(f'Начальный список: {list1}\n Произведение пар элементов списка: {list2}')