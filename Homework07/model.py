

def create_new_contact(data):
    with open('contacts.csv', 'a') as file:
        file.write(f'{data[0]};{data[1]};\n')
        return 'Новый контакт создан'

def find(name):
    with open('contacts.csv', 'r') as data:
        line = data.read().split('\n')
        book = {}
        for i in line[0:-1]:
            member = i.split(';')
            book[member[0]] = member[1]
        if name in book.keys():
            return book[name]
        else:
            return 'Контакт не найден'

def export_txt():
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        txt = ''
        for i in lines[0:-1]:
            member = i.split(';')
            txt += f'{member[0]} {member[1]}\n'
        with open('book_of_contacts.txt', 'w', encoding= 'utf-8') as book:
            book.write(txt)
        return 'Текстовый файл создан'


def export_xml():
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        xml = '<xml>\n'
        for i in lines[0:-1]:
            member = i.split(';')
            xml += f'    <name units = "{member[0]} ">{member[1]}</name>\n'
            xml += '</xml>'
        with open('book_of_contacts.xml', 'w', encoding= 'utf-8') as book:
            book.write(xml)
        return 'Xml-файл создан'


