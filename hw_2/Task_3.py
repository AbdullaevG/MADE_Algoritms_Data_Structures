def find_min_max(words, phase):
    max_value = words[0][phase]
    min_value = words[0][phase]

    for i in range(1, len(words)):
        if words[i][phase] > max_value:
            max_value = words[i][phase]

        if words[i][phase] < min_value:
            min_value = words[i][phase]

    return (ord(min_value), ord(max_value))


def num_sort(words, phase):
    min_item_ord = find_min_max(words, phase)[0]
    max_item_ord = find_min_max(words, phase)[1]

    letters_list = [words[i][phase] for i in range(len(words))]
    item_count_list = [0] * (max_item_ord - min_item_ord + 1)

    for i in range(len(letters_list)):
        item_count_list[ord(letters_list[i]) - min_item_ord] += 1

    start_indexes_list = [0] * len(item_count_list)
    for i in range(1, len(start_indexes_list)):
        start_indexes_list[i] = start_indexes_list[i - 1] + item_count_list[i - 1]

    sorted_with_phase = [0] * len(words)
    for word in words:
        letter = word[phase]
        sorted_with_phase[start_indexes_list[ord(letter) - min_item_ord]] = word
        start_indexes_list[ord(letter) - min_item_ord] += 1

    return sorted_with_phase


n, items_length, max_phase = map(int, input().split())

words = [0] * n
for i in range(n):
    words[i] = input()

for phase in range(items_length - 1, items_length - max_phase - 1, -1):
    words = num_sort(words, phase)

for i in range(len(words)):
    print(words[i])