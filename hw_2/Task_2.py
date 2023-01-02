def count_sort(array: list):
    assert type(array[0]) == int

    max_element = max(array)
    count_list = [0 for _ in range(max_element + 1)]

    for item in array:
        count_list[item] += 1

    j = 0
    for i in range(len(count_list)):
        while count_list[i] > 0:
            array[j] = i
            count_list[i] -= 1
            j += 1

    return array


sequence = list(map(int, input().split()))
print(*count_sort(sequence))


