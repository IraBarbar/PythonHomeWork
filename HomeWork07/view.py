

def show_all_list(dict_list: list):
    for contact in dict_list  :
        print( contact)  
        
        

def show_menu(list_menu):
    print(f'\tМеню:')
    for num, paragraph in enumerate(list_menu) :
        print( f'\t{num+1} - {paragraph}')
    num_paragraph =int(input('Выберите пункт меню: '))
    while (num_paragraph not in range(1,9)):
        num_paragraph = int(input('Ошибка! Выберите пункт меню: '))
    return num_paragraph     
    
        
 

    







    

