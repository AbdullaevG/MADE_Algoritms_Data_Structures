"""
Ограничение по времени на тест - 2 секунды
Ограничение по памяти на тест - 256 мегабайт

Ввод - стандартный ввод
Вывод - стандартный вывод

Пусть a1, a2, ..., an — числовая последовательность. Длина последовательности — это количество 
элементов этой последовательности. Последовательность ai1, ai2, ..., aik называется 
подпоследовательностью последовательности a, если 1 ≤ i1 < i2 < ... < ik ≤ n. 
Последовательность a называется возрастающей, если a1 < a2 < ... < an.

Вам дана последовательность, содержащая n целых чисел. Найдите ее самую длинную возрастающую 
подпоследовательность.

Входные данные
В первой строке задано одно число n (1 ≤ n ≤ 2000) — длина подпоследовательности. В следующей 
строке задано n целых чисел ai ( - 109 ≤ ai ≤ 109) — элементы последовательности.

Выходные данные
В первой строке выведите число k — длину наибольшей возрастающей подпоследовательности. 
В следующей строке выведите k чисел — саму подпоследовательность.

input:
8
1 4 1 5 3 3 4 2
output:
3
1 4 5

input:
3
1 2 3
output:
3
1 2 3
"""

import sys


def get_max(lst, start, end):
    temp_max = lst[start]
    idx = start
    
    for i in range(start, end):
        if lst[i] > temp_max:
            temp_max = lst[i]
            idx = i
            
    return (temp_max, idx)

def longest_increas_subseq(n, lst):
    dp = [1 for _ in range(n)]
    p = [i for i in range(n)]
    
    for i in range(1, n):
        max_dp = 0
        max_dp_idx = None
        
        for j in range(i-1, -1, -1):
            if lst[j] < lst[i]:
                
                if dp[j] > max_dp:
                    max_dp = dp[j]
                    max_dp_idx = j
        if max_dp:
            dp[i] = max_dp + 1
            p[i] = max_dp_idx
        
    return dp, p

def get_subseq(n, lst):
    dp, p = longest_increas_subseq(n, lst)
    max_len, idx = get_max(dp, 0, len(dp))
    subseq = []
    while True:

        if idx == p[idx]:
            subseq.append(lst[idx])
            break

        subseq.append(lst[idx])
        idx = p[idx]
    print(len(subseq))
    print(*subseq[::-1])
    

data = sys.stdin.readlines()
n = int(data[0].strip())
sequence = list(map(int, data[1].split()))

get_subseq(n, sequence)

