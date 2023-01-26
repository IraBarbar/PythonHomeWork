import view
import model


path =str('HomeWork08/' + view.input_class() + '.txt')
def start( ):
    global student
    global subject
    global path
    subject = view.choice_subject()
    student = model.open_data(path, subject)
    return student


def input_student(student):
    global journal
    global path
    while True:
        
        view.show_journal(student)
        num = view.name_student()
        list_keyes = []
        for key in student:
            n = key
            list_keyes.append(n)
        print(f' \t{num}. {list_keyes[num-1]} \t{student[list_keyes[num-1]]}')
        grade = view.grade()
        student[list_keyes[num-1]].append(grade)
        answer = ['Да','да']
        if input('Выйти из журнала? ') in answer:
            model.save_data(path,subject)
            exit()
     









