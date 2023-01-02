
def merge_lists(left: list, right: list):
    left_size = len(left)
    right_size = len(right)
    result = [0 for _ in range(left_size + right_size)]

    i, j = 0, 0
    while i + j < len(result):
        if (j == right_size) or (i < left_size and left[i] < right[j]):
            result[i + j] = left[i]
            i += 1
        else:
            result[i + j] = right[j]
            j += 1

    return result


def merge_sort(array):
    size = len(array)
    if size < 2:
        return array
    left = merge_sort(array[:size//2])
    right = merge_sort(array[size//2:])

    return merge_lists(left, right)

from test_function import test

test(merge_sort)
