
journal = dict()
student = dict()
 
def open_data(path, subject):
    global journal
    global student
    
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for line in data:
        line = line.strip()
        line = line.split(';')

        for i in range(len(data)):
            if line[0].lower == subject:
                journal[line[0]] = line[1]
    temp = []
    temp = line[1].split(',')
    temp = sorted(temp)
    
    for i in temp:
        i = i.split(':')
        i[1] = i[1].split(' ')
        i[1] = list(map(int, i[1]))
        student[i[0]] = i[1]
    return student

