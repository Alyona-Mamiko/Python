my_list = [23, None, -28, 'True', True, 3.56]


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)