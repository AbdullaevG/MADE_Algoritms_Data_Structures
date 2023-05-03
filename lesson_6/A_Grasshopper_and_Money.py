"""
time limit per test - 2 seconds
memory limit per test - 256 megabytes
input - standard input
output - standard output
The grasshopper is traveling from cell 1 to cell 𝑛. At the beginning, the grasshopper sits on cell 1. The cells are numbered from 1 to 𝑛. 
He can move from 1 to 𝑘  cells forward in one jump.
In each cell grasshopper can get or lose several gold coins (for each cell this number is known). Determine how the grasshopper needs to 
jump to maximize the total number of coins in the end. Consider that the grasshopper cannot jump backwards.

Input
The first line contains two integers 𝑛 and 𝑘 (3≤𝑛≤10000, 1≤𝑘≤10000) — the number of cells and the largest jump. The second line contains 𝑛−2
integers, the number of coins that the grasshopper gets on each cell, from the second to the 𝑛−1-th. If this number is negative, the grasshopper
loses coins. All the numbers do not exceed 10000  by absolute value.

Output
In the first line output the maximal number of coins. In the second line output the number of jumps. In the third line output the cells visited
by the grasshoper.
"""

import sys

SEPARATOR = "\n"
UNICODE = "utf-8"


def get_max(lst, start, end):
    temp_max = lst[start]
    idx = start
    
    for i in range(start, end):
        if lst[i] > temp_max:
            temp_max = lst[i]
            idx = i
            
    return (temp_max, idx)
    

def grasshopper_earn(n, k, lst):
    moneys = [0] + lst + [0]
    columns = [None for i in range(n)]
        
    for i in range(1, n):
        start_idx = max(0, i-k)
        prev_earn, idx = get_max(moneys, start_idx, i) 
        moneys[i] += prev_earn
        columns[i] = idx
    
    print(moneys[-1])
    
    visited = [n]
    temp_idx = columns[-1]
    while temp_idx is not None:
        visited.append(temp_idx + 1)
        temp_idx = columns[temp_idx]
        
    total_hops = len(visited) - 1
    print(total_hops)
    for i in range(total_hops, -1, -1):
        print(visited[i], end = " ")
        

def main():
    data  = sys.stdin.readlines()
    n, k = map(int, data[0].strip().split())
    lst = list(map(int, (data[1].strip().split())))
    grasshopper_earn(n, k, lst)

    
if __name__ == "__main__":
    main()
