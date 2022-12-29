# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
with open('polynominal_1.txt', 'w') as file:
    file.write('2*x^2 + 5*x^5')
with open('polynominal_2.txt', 'w') as file:
    file.write('4*x^4 + 2*x^3')

with open('polynominal_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('polynominal_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_polynominals.txt', 'w') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')