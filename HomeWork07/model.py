path = 'HomeWork07/basa_dannyh.txt'
list_bd = []
count = 1

def open_data(path):
    global list_bd
    global count
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()

    for line in data:
        line = line.replace('\n', '').replace(' ', '')
        line = line.split(';')
        bd_dict = dict()
        bd_dict['id'] = count
        bd_dict['lastname'] = line[1]
        bd_dict['name'] = line[2]
        bd_dict['phone'] = line[3]
        bd_dict['comment'] = line[4]
        list_bd.append(bd_dict)
        count += 1
    return list_bd


def set_bd(list_bd: list):
    global count
    new_contact = dict()
    new_contact['id'] = count
    new_contact['lastname'] = input('Введите фамилию: ')
    new_contact['name'] = input('Введите имя: ')
    new_contact['phone'] = input('Введите номер телефона: ')
    new_contact['comment'] = input('Комментарии: ')
    list_bd.append(new_contact)
    count += 1
    return list_bd


def change_contact(id_contact):
    global list_bd
    id_contact 
    for line in list_bd:
        for key, val in line.items():
            if val == id_contact:
                print(f'\n{line}')
                for num, key in enumerate(line, 1):
                    print(f'\t{num} - {key}')
                user =  int(
                    input('Введите пунк ключа, значение  которого вы хотите поменять: '))
                while user not in range(1,6):
                    user = int(
                        input('Введите пунк ключа, значение  которого вы хотите поменять: '))
                match user:
                    case 1:
                        user = 'id'
                    case 2:
                        user = 'lastname'
                    case 3:
                        user = 'name'
                    case 4:
                        user = 'phone'
                    case 5:
                        user = 'comment'

                print(f'\t{line[user]} - старое значение.')
                line[user] = str(input(f'\tВведите новое значение: '))
    return list_bd

def new_enumerate_id(list_bd):
    global count
    count = 1
    for line in list_bd:
        line['id'] = count
        count +=1
    return list_bd

def del_contact(list_bd: list, id_contact):
    global count
    old_len = len(list_bd)
    for line in list_bd:
        for key, val in line.items():
            if val == id_contact:
                print(f'\n{line}')
                list_bd.remove(line)
    if old_len != len(list_bd):
        new_enumerate_id(list_bd)
    return list_bd

def save_list(list_db):
    global path
    data_write = open(path, 'w', encoding='UTF-8')
    for i in range(len(list_bd)):
        string_bd = str()
        for key, val in list_bd[i].items():
            if key not in 'comment':
                string_bd = string_bd + str(val) + '; '
            else:
                string_bd = string_bd + str(val)
        data_write.write(f'{string_bd}\n')
    data_write.close()
