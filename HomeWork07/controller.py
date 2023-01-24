import model
import view

bd_list = model.open_data(model.path)

def menu():
    list_menu = [
        'показать все контакты',
        'добавить контакт',
        'изменить контакт',
        'удалить контакт',
        'найти контакт',
        'сохранить изменения в файле',
        'выйти из меню'
        ]
    return list_menu   

list_menu = menu()

def find_contact(list_bd):
    string_find = str(input('Поиск: '))
    clause = False
    for line in list_bd:
        for val in line.values():
            if string_find == val :
                print(line)
                clause = True      
    if clause == False:
        print(f'\tНичего не нашёл.\n')

def processing_request(num):
    match num:
        case 1:
            view.show_all_list(bd_list)
            processing_request(view.show_menu(list_menu))
        case 2:
            model.set_bd(bd_list)
            processing_request(view.show_menu(list_menu))
        case 3:
            model.change_contact()
            processing_request(view.show_menu(list_menu))
        case 4:
            model.del_contact(bd_list)
            processing_request(view.show_menu(list_menu))
        case 5:
            find_contact(bd_list)
            processing_request(view.show_menu(list_menu))
        case 6: 
            model.save_list(bd_list)
            processing_request(view.show_menu(list_menu))
        case 7:
            exit()





