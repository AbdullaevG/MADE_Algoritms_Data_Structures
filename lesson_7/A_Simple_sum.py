"""
A. Сумма простая

ограничение по времени на тест: 1 секунда
ограничение по памяти на тест: 512 мегабайт
ввод: стандартный ввод
вывод: стандартный вывод

Вам нужно научиться отвечать на запрос «сумма чисел на отрезке».

Массив не меняется. Запросов много. Отвечать на каждый запрос следует за O(1).

Входные данные
Размер массива — n и числа x, y, a_0, порождающие массив a: a_i=(x⋅a_{i−1}+y)mod2^16
Далее следует количество запросов m и числа z, t, b_0, порождающие массив b: b_i=(z⋅b_{i−1}+t)mod2^30.

Массив c строится следующим образом: c_i=b_i mod n.

Запросы: i-й из них — найти сумму на отрезке от min(c_{2i},c_{2i+1}) до max(c_{2i},c_{2i+1}) в массиве a.

Ограничения: 1≤n≤10^7, 0≤m≤10^7. Все числа целые от 0 до 2^16. t может быть равно −1.

Выходные данные
Выведите сумму всех сумм.

Пример
входные данные
3 1 2 3
3 1 -1 4
выходные данные
23

Примечание
𝑎={3,5,7},𝑏={4,3,2,1,0,230−1},𝑐={1,0,2,1,0,0},
запросы = {[0,1],[1,2],[0,0]}, суммы = {8,12,3}.

Префиксные суммы, как на лекции
"""


import sys

UPPER_BOUND_IN_ARRAY = 1 << 16
UPPER_BOUND_IN_QUERY = 1 << 30


def cum_sums(size: int, sequence: list) -> list:
    cum_sums_values = [0] * size
    temp_sum_value = 0
    
    for i in range(size):
        temp_sum_value += sequence[i]
        cum_sums_values[i] = temp_sum_value
        
    return cum_sums_values

def get_sum(cum_sums_list, left, right) -> int:
    
    if left > 0:
        return cum_sums_list[right] - cum_sums_list[left - 1]
    
    else:
        return cum_sums_list[right]

def main():

    data = sys.stdin.readlines()
    
    n, x, y, seq_0 = map(int, data[0].strip().split())
    m, z, t, query_0 = map(int, data[1].strip().split())
    
    query_list = [query_0] + [0] * (2 * m - 1)
    sequence = [seq_0] + [0] * (n - 1)
    
    for i in range(1, n):
        sequence[i] = (x * sequence[i - 1] + y) % UPPER_BOUND_IN_ARRAY
        
    cum_sums_list = cum_sums(n, sequence)
    total_sum = 0
    
    for i in range(1, 2 * m):
        query_list[i] = (z * query_list[i - 1] + t) % UPPER_BOUND_IN_QUERY
        
        if i % 2 == 1:
            left, right = min(query_list[i - 1] % n, query_list[i] % n), max(query_list[i - 1] % n, query_list[i] % n)
            total_sum += get_sum(cum_sums_list, left, right)  
        
    print(total_sum)

    
if __name__ == "__main__":
    main()
