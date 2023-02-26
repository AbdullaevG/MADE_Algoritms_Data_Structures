"""
B. Быстрый поиск в массиве

ограничение по времени на тест: 1 секунда
ограничение по памяти на тест: 512 мегабайт
ввод: стандартный ввод
вывод: стандартный вывод

Дан массив из 𝑛 целых чисел. Все числа от −10^9 до 10^9.
Нужно уметь отвечать на запросы вида «Cколько чисел имеют значения от 𝑙 до 𝑟»?

Входные данные
Число 𝑛 (1≤𝑛≤10^5). Далее 𝑛 целых чисел.
Затем число запросов 𝑘 (1≤𝑘≤10^5).
Далее 𝑘 пар чисел 𝑙,𝑟 (−10^9≤𝑙≤𝑟≤10^9) — собственно запросы.

Выходные данные
Выведите 𝑘 чисел — ответы на запросы.
Пример
входные данные
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2
выходные данные
5 2 2 0
"""

import sys


def left_bound(sequence: list, item: int, left_index=-1):
    right_index = len(sequence)

    while right_index - left_index > 1:
        middle = (left_index + right_index) // 2

        if sequence[middle] < item:
            left_index = middle
        else:
            right_index = middle

    return left_index


def right_bound(sequence: list, item: int, left_index):
    return left_bound(sequence, item + 1, left_index=left_index)


def fast_search(sequence: list, left_item: int, right_item: int):
    if left_item > right_item:
        return 0

    left_index = left_bound(sequence, left_item)
    right_index = right_bound(sequence, right_item, left_index=left_index)

    return right_index - left_index


def main():
    n = int(sys.stdin.readline())
    sequence = sorted(list(map(int, sys.stdin.readline().split())))
    k = int(sys.stdin.readline())
    for _ in range(k):
        lower, upper = map(int, sys.stdin.readline().split())
        print(fast_search(sequence, lower, upper), end=' ', flush=True)


if __name__ == "__main__":
    main()
