

def add_person(card):
    full_name, position, salary = card
    with open('database.csv', 'a') as data:
        member = f'{full_name};{position};{salary}\n'
        data.write(member)
    return 'Новый сотрудник занесен в базу данных'


# def add_person(person):
#     with open('database.csv', 'a') as file:
#         file.write(f'{person[0]};{person[1]}; {person[2]}\n')
#         return 'Новый сотрудник занесе в базу данных'

def find_person(key):
    with open('database.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                full_name, position, salary = i.split(';')
                return f'{full_name}\n{position}\n{salary}'
            else:
                return 'Not found'

def export_xml():
    with open('database.csv', 'r') as data:
        lines = data.read().split('\n')
        xml = '<xml>\n'
        for i in lines[0:-1]:
            member = i.split(';')
            xml += f'<name = "{member[0]}">\n'\
                    f'   <position>"{member[1]}"<position>\n'\
                    f'   <salary>"{member[2]}"<salary>\n'
            xml += '</xml>'
        with open('database.xml', 'w', encoding= 'utf-8') as book:
            book.write(xml)
        return 'Xml-файл создан'

