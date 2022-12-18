# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3]
# - список на основе n, а позиции элементов lst2=[3,1].

import random

user_number = int(input('Введите число: '))
n_list = [random.randint(-user_number, user_number + 1) for i in range(user_number)]
print(n_list)
data = open('file.txt', 'w')
while True:
    line = input('Укажите позицию для вычисления: ')
    if line == '':
        break
    data.write(line + '\n')
data.close()

result = 1
data = open('file.txt', 'r')
for line in data:
    if line == '':
        break
    result *= n_list[int(line)]
data.close()
print(result)
