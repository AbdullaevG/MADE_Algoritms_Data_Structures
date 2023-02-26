'''
A. Приближенный двоичный поиск
ограничение по времени на тест: 2 секунды
ограничение по памяти на тест: 256 мегабайт
ввод: стандартный ввод
вывод: стандартный вывод

Даны два массива. Первый массив отсортирован по неубыванию,
второй массив содержит запросы — целые числа.
Для каждого запроса выведите число из первого массива наиболее близкое (то есть с минимальным модулем разности)
к числу в этом запросе .
Если таких несколько, выведите меньшее из них.

Входные данные
В первой строке входных данных содержатся числа n и k (0<n,k≤10^5).
Во второй строке задаются n чисел первого массива, отсортированного по неубыванию,
а в третьей строке — k чисел второго массива.
Каждое число в обоих массивах по модулю не превосходит 2·10^9 .

Выходные данные
Для каждого из k чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному.
Если таких несколько, выведите меньшее из них.
Пример
входные данные
5 5
1 3 5 7 9
2 4 8 1 6
выходные данные
1
3
7
1
5
'''


def left_bound(sequence: list, item: int):
    left_index = 0
    right_index = len(sequence) - 1

    while right_index - left_index > 1:
        middle = (left_index + right_index) // 2
        if sequence[middle] < item:
            left_index = middle
        else:
            right_index = middle

    return left_index


def right_bound(sequence: list, item: int):
    return left_bound(sequence, item + 1)


def approximate_bin_search(sequence:list, item:int):
    left_index = left_bound(sequence, item)
    right_index = right_bound(sequence, item)

    index_correction = int(right_index == left_index)
    right_index, left_index = right_index + index_correction, left_index - index_correction

    left_item = sequence[left_index + 1]
    right_item = sequence[right_index]

    if item - left_item <= right_item - item:
        return left_item

    return right_item


def main():
    n, k = map(int, input().split())
    sequence = list(map(int, input().split()))
    items = list(map(int, input().split()))

    for item in items:
        print(approximate_bin_search(sequence, item))


if __name__ == "__main__":
    main()