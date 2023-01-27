
def show_menu():
    return int(input('1 - Внести в базу нового сотрудника \n' \
                   '2 - Найти информацию о сотруднике \n' \
                   '3 - Экспорт базы данных сотдуников в формет  xml\n' \
                   '0 - Выход\n'))

def find_person():
    return input('Введите имя сотрудника: ')

def add_person():
    full_name = input('Введите имя сотрудника: ')
    position = input('Введите должность сотрудника: ')
    salary = input('Введите зарплату сотрудника: ')
    return (full_name, position, salary)

def show(result):
    print(result)