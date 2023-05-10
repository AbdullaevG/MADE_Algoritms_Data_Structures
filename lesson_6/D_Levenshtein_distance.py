"""
time limit per test - 2 seconds
memory limit per test - 256 megabytes

input - standard input
output - standard output

You are given a string. You can perform operations of three types:

 1. Replace one symbol by another.
 2. Delete any symbol.
 3. Insert any symbol in any position of the string.
 
The smallest number of operations to be performed in order to transform one string to another 
one is named edit distance or Levenshtein distance.

Find the Levenshtein distance between two given strings.

Input
The input contains two lines that contain two strings. The length of each string does 
not exceed 1_000 symbols and they consist of only uppercase Latin letters.
"""

import sys


def levenshtein_distance(word_1:str, word_2:str):
    grid = [[i + j if j * i == 0 else 0 for j in range(len(word_2) + 1)] for i in range(len(word_1) + 1)]
    
    for i in range(1, len(word_1) + 1):
        for j in range(1, len(word_2) + 1):
            
            if word_1[i - 1] == word_2[j - 1]:
                grid[i][j] = grid[i - 1][j - 1]
                
            else:
                grid[i][j] = 1 + min(grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1])
                
    return grid[len(word_1)][len(word_2)]


data = sys.stdin.readlines()
word_1 = data[0].strip()
word_2 = data[1].strip()
print(levenshtein_distance(word_1, word_2))
