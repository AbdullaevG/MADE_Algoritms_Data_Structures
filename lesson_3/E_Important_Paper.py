'''
You have two copy machines and one copy of very important paper. You need to get n
more copies of this paper. First copy machine copies one new copy for x seconds,
second one for y seconds. You can use both copy machines at the same time and copy
not only original paper, but copy too.

You need to find minimal time to get n copies

Input
The first line contains three integers n, x and y(1≤n≤2·10^8, 1≤x,y≤10).

Output
Print one number — minimal time in seconds to get n copies.

Examples
input
4 1 1
output
3
input
5 1 2
output
4
'''


def func(time):
    global time_1, time_2, num_of_copies

    time_1, time_2 = min(time_1, time_2), max(time_1, time_2)
    copies_for_time = time // time_1 + (time - time_1) // time_2

    return copies_for_time >= num_of_copies


def get_min_time():
    left_edge = 1
    right_edge = 2

    while not func(right_edge):
        right_edge *= 2

    while right_edge - left_edge >= 1:
        middle = (left_edge + right_edge) // 2

        if not func(middle):
            left_edge = middle + 1
        else:
            right_edge = middle

    return right_edge


num_of_copies, time_1, time_2 = map(int, input().split())
print(get_min_time())