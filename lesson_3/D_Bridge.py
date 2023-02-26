'''
There was a flood in the town of Graffiti Walls! During the disaster the wooden bridge across
the river was demolished. Bipper and his sister Maple were happy to help citizens but that
wasn't enough.
Now is your turn to save this wonderful town! There are n new timbers prepared for you and
the bridge has to consist of exactly k timbers. You can cut timbers into smaller ones with
integer length, but you can't combine them into one, because that would not be solid enough.
The selected k timbers must have the same length.

Your task is to find maximal width of the bridge.

Input
The first line of input contains two integers n and k (1≤n,k≤10001)

Each of the following n lines contain one integer ai — the length of the i-th timber (1<= a_i <= 10**8).

Output
The output must contain one integer — maximal width of the bridge.

If there is no way to make a bridge with the given constraints, answer should be 0.
input
4 11
802
743
457
539

output
200
'''


import sys


def func(length):
    global lengths_list, K
    num_of_ropes = 0

    for i in range(len(lengths_list)):
        num_of_ropes += int(lengths_list[i] / length)

    return num_of_ropes >= K


def get_max_length():
    left_edge = 1
    if not func(left_edge):
        return 0

    right_edge = 2
    while func(right_edge):
        right_edge *= 2

    while right_edge - left_edge >= 1:

        middle = (left_edge + right_edge) // 2

        if func(middle):
            left_edge = middle + 1
        else:
            right_edge = middle

    return right_edge - 1


def main():
    data = sys.stdin.readlines()
    N, K = map(int, data[0].split())
    lengths_list = [int(data[i]) for i in range(1, N + 1)]
    print(get_max_length())


if __name__ == "__main__":
    main()


