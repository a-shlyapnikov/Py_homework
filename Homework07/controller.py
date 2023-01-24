import view
import model

def show(res):
    view.view(res)




def create_contact():
    return model.create_new_contact(view.add_new_contact())

def find_contact():
    return model.find(view.find())

def export_contacts_txt():
    return model.export_txt()

def export_contacts_xml():
    return model.export_xml()

def main_menu(result):
    if result == '0':
        show('Выход...')
    else:
        if result == '1':
            show(create_contact())
        elif result == '2':
            show(find_contact())
        elif result == '3':
            show(export_contacts_txt())
        elif result == '4':
            show(export_contacts_xml())
        else:
            show('Ошибка ввода')
        main_menu(view.show_menu())

