"""
A. Simple sum

time limit per test: 1 second
memory limit per test - 512 megabytes
input - standard input
output - standard output

You have to answer requests "sum of numbers on the segment".
Array doesn't change. There're many requests. You should answer on each in $O(1)$  time.

Input
First line contains four integers:  — n, x, y, a_0, length of the array and numbers which generates array a: a_i=(x⋅a_{i−1}+y)mod2^16
Next line contains four integers: m, z, t, b_0, number of requests and numbers which generates array b: b_i=(z⋅b_{i−1}+t)mod2^30.

Array c is generating in the following way: c_i=b_i mod n.

Request number i is to find sum on segment from min(c_{2i},c_{2i+1}) до max(c_{2i},c_{2i+1}) in the array a.

Limit: 1≤n≤10^7, 0≤m≤10^7. All other number are from 0 to  2^16. t  can also be equal to −1.

Output
Output sum of all sums.

Example
input
3 1 2 3
3 1 -1 4
output
23

Note
𝑎={3,5,7},𝑏={4,3,2,1,0,230−1},𝑐={1,0,2,1,0,0},
Requests = {[0,1],[1,2],[0,0]}, sumsы = {8,12,3}.
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
