def bubble_sort(array: list):
    size = len(array)

    while size > 0:
        for i in range(1, size):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
        size -= 1

    return array

from test_function import test
test(bubble_sort)
