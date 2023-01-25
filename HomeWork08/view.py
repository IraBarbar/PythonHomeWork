
def input_class():
    num_class = input('Введите номер и букву класса: ')
    list_class = ['7Б']
    num_class = num_class.replace(' ','')
    num_class = num_class.upper()
    if num_class not in list_class:
        print(f'Такого класса нет! Список классов: ' , *list_class)
    while num_class not in list_class:
        num_class = input('Введите номер и русскую букву класса: ')
    return num_class       

def choice_subject():
    subject_list =[
        'математика',
        'русская литература',
        'русский язык',
        'химия',
        'биология']
    print(f'Выберите предмет: ')
    subject_list = sorted(subject_list)
    for num, name in enumerate(subject_list,1):
        print(f'\t{num} {name}')
    num = int(input('Введите номер предмета: '))
    subject = subject_list[num-1]
    
    print(f'\n\tЖурнал по предмету "{subject.upper()}":')
    return subject
    
def show_journal(student):
    i = 1
    for key,val,  in student.items():
        n = key
        print(  f'\t{i}. {key}   \t{val}')
        i+=1    
    return     

def name_student():
    num =int(input('Кто идет отвечать? Введите порядковый номер студента: ')) 
    return num   

# def show_name()