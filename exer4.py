my_list = [(8,3),(7,5),(6,4),(1,9)]

def tuples(item):
    return item[1]

my_list.sort(key=tuples)
print(my_list)