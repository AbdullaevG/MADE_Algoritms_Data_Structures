from random import randint

def hoar(order: int, array: list):

    if len(array) == 1:
        return array[0]

    rand_index = randint(0, len(array) - 1)
    rand_item = array[rand_index]
    left_array = [element for element in array if element < rand_item]
    right_array = [element for element in array if element >= rand_item]

    if order < len(left_array):
        return hoar(order, left_array)
    else:
        order = order - len(left_array)
        return hoar(order, right_array)


