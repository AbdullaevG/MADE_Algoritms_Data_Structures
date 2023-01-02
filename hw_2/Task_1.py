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


array = [10, 11, 9, 8, 6, 0, 12]
print(hoar(4, array))

def get_k_th_order(array: list, left_edge: int, right_edge: int, order: int):
    assert (len(array) > right_edge and right_edge > left_edge and (right_edge - left_edge >= order))
    sub_array = array[left_edge:right_edge]
    return hoar(order, sub_array)


print(get_k_th_order([1, 2, 3, 4, 5], 0, 2, 1))

n = int(input())
seq = list(map(int, input().split()))

request_number = int(input())
for _ in range(request_number):
    start, end, order = map(int, input().split())
    print(find_order(order, seq, start, end))