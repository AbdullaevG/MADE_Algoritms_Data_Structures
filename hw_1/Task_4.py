import random

def quick_sort(array):
    size = len(array)
    if size < 2:
        return array

    rand_idx = random.randint(0, size-1)
    rand_element = array[rand_idx]
    left = [element for element in array if element < rand_element]
    middle = [element for element in array if element == rand_element]
    right = [element for element in array if element > rand_element]

    return quick_sort(left) + middle + quick_sort(right)

from test_function import test
test(quick_sort)