# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

user_number = int(input('Введите число: '))
i = 2
lst = []
a = user_number
while i <= a:
    if a % i == 0:
        lst.append(i)
        a //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {user_number} приведены в списке: {lst}")