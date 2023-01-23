path = 'HomeWork07/basa_dannyh.txt'

def open_data(path):
    global list_bd
    list_bd = []
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        
    for line in data:
        line = line.replace('\n', '')
        line = line.split(';')
        
        bd_dict = dict()
        bd_dict['lastname'] = line[0]
        bd_dict['name'] = line[1]
        bd_dict['phone'] = line[2]
        bd_dict['comment'] = line[3]
        list_bd.append(bd_dict)
    return list_bd  
        
        

        
    
def set_bd(list_bd: list):
    new_contact = dict()
    new_contact['lastname'] = input('Фамилия: ')
    new_contact['name'] = input('Имя: ')
    new_contact['phone'] = input('Номер телефона: ')
    new_contact['comment'] = input('Комментарии: ')
    list_bd.append(new_contact)
    
    return list_bd

def save_list(list_bd):
    data_write = open('HomeWork07/basa_dannyh.txt', 'w', encoding='UTF-8')
    for i in range(len(list_bd)) :
        string_bd =str()
        for key, val in list_bd[i].items():
            if key not in 'comment':
                string_bd = string_bd + str(val) + '; '
            else:
                string_bd = string_bd + str(val)
        data_write.write(f'{string_bd}\n')
    data_write.close()


    


 
        
    

