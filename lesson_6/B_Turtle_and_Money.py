"""
time limit per test - 2 seconds
memory limit per test - 256 megabytes

input - standard input
output - standard output

There is a rectangular field of size n×m . The turtle wants to move from cell (1, 1) to cell (n, m), in one 
step she can move to the next cell down or right.  For each passed cell, the turtle gains (or loses) several gold coins (this number is known for each cell).

Determine what the maximum number of coins Turtle can collect on the way and how she needs to go for it.

Input
The first line contains two integers: n and m (2≤n,m≤1000). Each of the following n lines contains m numbers aij (|aij|≤10), which indicate the 
number of coins received by the turtle on each cell. If this number is negative, the turtle loses coins.

Output
In the first line, output maximal number of coins that turtle can collect. In the second output the commands to be executed by the turtle, 
without spaces : the letter «R» indicates a step to the right, and the letter «D» a step down.
"""
import sys
 
SEPARATOR = "\n"
UNICODE = "utf-8"


def spyder_earn(n, m, grid_values):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    p = [[None for _ in range(m)] for _ in range(n)]
    
    dp[0][0] = grid_values[0][0]
    p[0][0] = None
    
    for i in range(n):
        for j in range(m):
            temp_cell_money = grid_values[i][j]
            
            if i==0 and j > 0:
                dp[i][j] = dp[i][j-1] + temp_cell_money
                p[i][j] = (i, j-1)
            
            if j==0 and i > 0:
                dp[i][j] = dp[i-1][j] + temp_cell_money
                p[i][j] = (i-1, j)
            
            if i > 0 and j > 0:
                
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + temp_cell_money
                    p[i][j] = (i-1, j)
                
                else:
                    dp[i][j] = dp[i][j-1] + temp_cell_money
                    p[i][j] = (i, j-1)
    
    steps = ""
    x, y = n-1, m-1
    temp_point = p[x][y]
    while temp_point is not None:
        prev_x, prev_y = temp_point
        if prev_x == x:
            steps += "R"
            y -= 1
        else:
            steps += "D"
            x -= 1
        temp_point = p[x][y]
        
    return dp[-1][-1], steps[::-1]


def main():
    data  = sys.stdin.readlines()

    n, k = map(int, data[0].strip().split())

    grid_values = [list(map(int, item.strip().split())) for item in data[1:]]
    dp, s = spyder_earn(n, k, grid_values)
    print(dp)
    print(s)
    
if __name__ == "__main__":
    main()

