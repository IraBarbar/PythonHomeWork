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
        random_list.append(random.randint(start,finish))
    return random_list

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

        
