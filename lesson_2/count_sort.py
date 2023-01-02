
def count_sort(array: list):
    assert type(array[0]) == int

    max_element, min_element = max(array), min(array)
    count_list = [0 for _ in range(max_element - min_element + 1)]

    for item in array:
        count_list[item - min_element] += 1

    j = 0
    for i in range(len(count_list)):
        while count_list[i] > 0:
            array[j] = i + min_element
            count_list[i] -= 1
            j += 1

    return array

def test(algorithm):

    array_1 = [1, 1, 1, 2, 1, -2, 1, 2, 2]
    result_1 = algorithm(array_1)
    if result_1 == [-2, 1, 1, 1, 1, 1, 2, 2, 2]:
        print("test#1___ok!")
    else:
        print("test#1___fail")
        print("Correct_result: ", [-2, 1, 1, 1, 1, 1, 2, 2, 2])
        print("Algorithm output: ", result_1)

    array_2 = [10, 9, 8, 10, 9, 8]
    result_2 = algorithm(array_2)
    if result_2 == [8, 8, 9, 9, 10, 10]:
        print("test#2___ok!")
    else:
        print("test#2___fail")
        print("Correct_result: ", [8, 8, 9, 9, 10, 10])
        print("Algorithm output: ", result_2)


    array_3 = [0, 0, -100, 0]
    result_3 = algorithm(array_3)
    if result_3 == [-100, 0, 0, 0]:
        print("test#3___ok!")
    else:
        print("test#3___fail")
        print("Correct_result: ", [-100, 0, 0, 0])
        print("Algorithm output: ", result_3)

    array_4 = [2]
    result_4 = algorithm(array_4)
    if result_4 == [2]:
        print("test#4___ok!")
    else:
        print("test#4___fail")
        print("Correct_result: ", [2])
        print("Algorithm output: ", result_4)


test(count_sort)

# sequence = list(map(int, input().split()))
# print(*count_sort(sequence))