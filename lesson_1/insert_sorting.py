# 286 мс

def insert_sort(array):
    size = len(array)
    for i in range(1, size):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

test_files = ["test_1.txt", "test_2.txt"]

for test_file in test_files:
    with open(test_file, "r", encoding="utf-8") as file:
        data = file.readlines()
        N = int(data[0].strip())
        array = list(map(int, data[1].split()))
        print(*insert_sort(array))