# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально и особенность данного языка программирования.
# ваш ответ может не совпадать с примером(может получитя 0,20))
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []
for i in range(len(list1)):
    list2.append(round(list1[i] - int(list1[i]), 3))
print(f'Разница между минимальным и максимальным значениями равна {max(list2) - min(list2)}')
a = 1.1

