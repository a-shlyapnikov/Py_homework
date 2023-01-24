

def add_new_contact():
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    return (name, phone)

def find():
    return input('Введите имя: ')

def show_menu():
    return input('1 - Создать новый контакт \n' \
                   '2 - Найти контакт \n' \
                   '3 - Экспорт контатов в формате txt\n' \
                   '4 - Экспорт контактов в формате  xml\n' \
                   '0 - Выход\n')

def view(message):
    return print(message)