

def show_all_list(dict_list: list):
    for i in range(len(dict_list)) :
        print( *dict_list[i].values())
        

def show_menu(list_menu):
    print(f'\tМеню:')
    for num, paragraph in enumerate(list_menu) :
        print( f'\t{num+1} - {paragraph}')
    num_paragraph = int(input('Выберите пункт меню: '))
    print()
    return num_paragraph     

    







    

