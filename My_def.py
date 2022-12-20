def random_list_float(lenth, start, finish):
    import random
    random_list = []
    for _ in range(lenth):
        index = random.randint(0,3)
        random_list.append(round(random.uniform(start,finish),index))
    return random_list

def random_list_int(lenth, start, finish):
    import random
    random_list = []
    for _ in range(lenth):
        index = 0
        random_list.append(int(random.uniform(start,finish)))
    return random_list