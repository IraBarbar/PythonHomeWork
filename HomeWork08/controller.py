import view
import model


def start( ):
    global student
    global subject
    global path
    path =str('HomeWork08/' + view.input_class() + '.txt')
    subject = view.choice_subject()
    student = model.open_data(path, subject)
    return student


def input_student(student):
    num = view.name_student()
    list_keyes = []
    for key in student:
        n = key
        list_keyes.append(n)
    print(f' \t{num}. {list_keyes[num-1]} \t{student[list_keyes[num-1]]}')
    
     









