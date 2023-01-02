def merge_lists(left: list, right: list):
    global inversion

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
            if i != left_size:
                inversion += (left_size - i)


    return result

inversion = 0

def merge_sort(array):
    size = len(array)
    if size < 2:
        return array
    left = merge_sort(array[:size//2])
    right = merge_sort(array[size//2:])

    return merge_lists(left, right)

array = [5, 4, 2, 1]
merge_sort(array)
print(inversion)

#n = int(input())
#seq = list(map(int, input().split()))
#seq = merge_sort(seq)
#print(num_inv)
