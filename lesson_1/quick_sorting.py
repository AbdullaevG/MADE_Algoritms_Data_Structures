import random

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot_index = random.randint(0, len(lst) - 1)
        pivot_element = lst[pivot_index]

        left = [item for item in lst if item < pivot_element]
        middle = [item for item in lst if item == pivot_element]
        right = [item for item in lst if item > pivot_element]

        return quick_sort(left) + middle + quick_sort(right)

test_files = ["test_1.txt", "test_2.txt"]

for test_file in test_files:
    with open(test_file, "r", encoding="utf-8") as file:
        data = file.readlines()
        N = int(data[0].strip())
        array = list(map(int, data[1].split()))
        print(*quick_sort(array))