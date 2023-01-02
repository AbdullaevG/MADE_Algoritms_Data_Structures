
def sort_pairs(sequence: list):
    assert type(sequence[0]) == tuple

    max_first = sequence[0][0]
    min_first = sequence[0][0]

    for i in range(1, len(sequence)):
        if sequence[i][0] > max_first:
            max_first = sequence[i][0]

        if sequence[i][0] < min_first:
            min_first = sequence[i][0]

    count_list = [0 for _ in range(max_first - min_first + 1)]
    for i in range(len(sequence)):
        count_list[sequence[i][0] - min_first] += 1

    elements_start_idx = [0 for _ in range(max_first - min_first + 1)]
    for i in range(1, len(elements_start_idx)):
        elements_start_idx[i] = elements_start_idx[i - 1] + count_list[i - 1]

    result = [None for _ in range(len(sequence))]
    for i in range(0, len(sequence)):
        result[elements_start_idx[sequence[i][0]]] = sequence[i]
        elements_start_idx[sequence[i][0]] += 1

    return result


print(sort_pairs([(0, 1), (5, 1), (0, 2), (0, 1), (2, 3), (1, 11), (3, 2), (3, 1)]))
