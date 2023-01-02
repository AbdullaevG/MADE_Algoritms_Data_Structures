
def get_digit(position, number, base = 10):
    digit = (number//base**position) % base
    return digit


def digit_sort(array: list, base = 10):
    K = len(str(max(array)))
    count_array = [[] for _ in range(base)]
    p = [i for i in range(len(array))]

    for k in range(K):
        temp_digits = [get_digit(k, array[p[i]], base) for i in range(len(p))]
        for i in range(len(p)):
            count_array[temp_digits[i]].append(p[i])
        p = []
        for i in range(len(count_array)):
            p += count_array[i]
            count_array[i] = []
    result = [array[p[i]] for i in range(len(p))]

    return result


print(digit_sort([109, 10, 42, 98, 89, 23, 11, 37]))
print(digit_sort([987, 11, 2, 1, 0, 23, 2333, 876, 15]))