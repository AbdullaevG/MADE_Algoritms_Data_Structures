# 186 мс

def bubble_sort(array: list):
    last_idx = len(array)-1
    while last_idx > 0:
        for i in range(last_idx):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        last_idx -= 1
    return array


test_files = ["test_1.txt", "test_2.txt"]

for test_file in test_files:
    with open(test_file, "r", encoding="utf-8") as file:
        data = file.readlines()
        N = int(data[0].strip())
        array = list(map(int, data[1].split()))
        print(*bubble_sort(array))