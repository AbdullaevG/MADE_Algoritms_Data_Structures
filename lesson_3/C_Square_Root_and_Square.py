"""
C. Квадратный корень и квадратный квадрат

ограничение по времени на тест: 2 секунды
ограничение по памяти на тест: 256 мегабайт
ввод: стандартный ввод
вывод: стандартный вывод

Найдите такое число x, что x**2+sqrt(x)=C, с точностью не менее 6 знаков после точки.

Входные данные
В единственной строке содержится вещественное число 1.0≤C≤10^10.

Выходные данные
Выведите одно число — искомый x.

Пример 1
входные данные
2.0000000000
выходные данные
1.0
Пример 2
входные данные
18.0000000000
выходные данные
4.0
"""

import sys
import math

EPS = 10 ** (-7)
RIGHT_EDGE = 1
LEFT_EDGE = 0


def func(argument: float):
    return argument ** 2 + argument ** 0.5


def find_root(func_value: float):
    left_edge = LEFT_EDGE
    right_edge = RIGHT_EDGE

    while func(right_edge) <= func_value:
        right_edge *= 2

    num_iter = int(math.log2((right_edge - left_edge) / EPS))

    for _ in range(num_iter):
        middle = (left_edge + right_edge) / 2
        if func(middle) <= func_value:
            left_edge = middle
        else:
            right_edge = middle

    return round((right_edge + left_edge) / 2, 6)


def main():
    inp = float(sys.stdin.readline())
    print(find_root(inp))


if __name__ == "__main__":
    main()