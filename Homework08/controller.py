import model as m
import view as v

def main(result):
    if result == 0:
        v.show('Выход...')
    else:
        if result == 1:
            v.show(m.add_person(v.add_person()))
        elif result == 2:
            v.show(m.find_person(v.find_person()))
        elif result == 3:
            v.show(m.export_xml())
        else:
            v.show('Ошибка ввода')
        main(v.show_menu())