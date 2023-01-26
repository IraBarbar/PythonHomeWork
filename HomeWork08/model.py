
journal = dict()
student = dict()


def open_data(path, subject):
    global journal
    global student

    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    temp = []
    for line in data:
        line = line.strip()
        line = line.split(';')
        for i in range(len(data)):
            journal[line[0]] = line[1]
            if line[0].lower == subject:
                journal[subject] = line[1]
    temp = journal[subject].split(',')
    temp = sorted(temp)
    for i in temp:
        i = i.split(':')
        i[1] = i[1].split(' ')
        i[1] = list(map(int, i[1]))
        student[i[0]] = i[1]
    return student

def save_data(path, subject):
    global journal
    data_write = open(path, 'w', encoding='UTF-8')
    string_journal = str()
    for key, val in journal.items():
        string_journal = str(key) + ';'
        if key != subject:
            string_journal = string_journal + val
        else:
            for k, v in student.items():
                string_journal = string_journal + str(k) + ':'
                for i in v:
                    string_journal = string_journal + str(i) + ' '
                string_journal = string_journal[:-1] + ','
            string_journal = string_journal[:-1]      
        data_write.write(f'{string_journal}\n')
    data_write.close()
                    
    
