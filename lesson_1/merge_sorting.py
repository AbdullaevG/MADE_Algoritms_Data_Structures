# 46 мс

def merge(left, right):
    left_length, right_length = len(left), len(right)

    i, j = 0, 0
    merged = [None for k in range(left_length + right_length)]
    while i + j < left_length + right_length:
        if j == right_length or (i < left_length and left[i] < right[j]):
            merged[i + j] = left[i]
            i += 1
        else:
            merged[i + j] = right[j]
            j += 1
    return merged


def merge_sort(array):

    size = len(array)
    if size < 2:
        return array
    left = merge_sort(array[:size//2])
    right = merge_sort(array[size//2:])
    return merge(left, right)

test_files = ["test_1.txt", "test_2.txt"]
for test_file in test_files:
    with open(test_file, "r", encoding="utf-8") as file:
        data = file.readlines()
        N = int(data[0].strip())
        array = list(map(int, data[1].split()))
        print(*merge_sort(array))

