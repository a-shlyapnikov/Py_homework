import random


def mix_list(list):
    mix_lst = list[:]
    for i in range(len(mix_lst)):
        j = random.randint(0, len(mix_lst) - 1)
        temp = mix_lst[i]
        mix_lst[i] = mix_lst[j]
        mix_lst[j] = temp
    return mix_lst


user_number = int(input('Введите число: '))
lst = [random.randint(-user_number, user_number + 1) for i in range(user_number)]
print(lst)
mix_lst = mix_list(lst)
print(mix_lst)
