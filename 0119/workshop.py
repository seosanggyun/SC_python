
int_list = list(map(int, input().split()))

def list_sum(a):
    total = 0
    for i in int_list:
        total += i
    print(total)

list_sum(int_list)

dict_list = [{'name': 'harry', 'age': 5}, {'name': 'sang', 'age': 29}]

def dict_list_sum(a):
    total = 0
    for i in dict_list:
        total += i['age']
    print(total)

dict_list_sum(dict_list)

all_list = ([1], [2, 3], [4, 5, 6], [7, 8, 9, 10])

def all_list_sum(a):
    total = 0
    for i in all_list:
        for j in i:
            total += j
    print(total)


all_list_sum(all_list)        