"""
B. Postfix Notation
time limit per test - 1 second
memory limit per test - 256 megabytes
input - standard input
output - standard output

In a postfix notation (Reverse Polish notation), two operands are followed by an operation. For example, the sum of 
two numbers A and B is written as A B +.  The expression B C + D * means (B + C) * D, and the expression A B C + D * + means A + (B + C) * D. 
The advantage of a postfix notation is that it does not require brackets and additional operator precedence agreements for its reading.

An expression is given in the reverse Polish notation. Calculate the result.

Input
The input contains the expression in the postfix notation containing single-digit numbers and the operations +, -, *. 
The string contains no more than 100 numbers and operations.

Output
Output the result of the expression. It is guaranteed that the result of the expression, as well as the results of all 
intermediate calculations is less than 231 by an absolute value.
"""

class Vector:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.elements = [None for _ in range(self.capacity)]

    def get(self, i):
        if (i < 0) or (i > self.size):
            return None
        return self.elements[i]

    def add(self, item):
        if self.size + 1> self.capacity:
            self.ensure_capacity()

        self.elements[self.size] = item
        self.size += 1

    def ensure_capacity(self, scale=2):
        self.capacity = int(self.capacity * scale)
        new_elements = [None for _ in range(self.capacity)]
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements

    def print_elements(self):
        for i in range(self.size):
            print(self.elements[i], end = " ")

    def erase_last(self):
        if self.size > 0:
            last = self.elements[self.size-1]
            self.elements[self.size-1] = None
            self.size -= 1
            if 2 <= self.size <= self.capacity//4:
                self.ensure_capacity(scale=0.25)
            return last


class StackVector:
    def __init__(self, capacity):
        self.vector = Vector(capacity)
        self.capacity = self.vector.capacity
        self.size = self.vector.size

    def push(self, item):
        self.vector.add(item)

    def pop(self):
        return self.vector.erase_last()

    def get_size(self):
        return self.vector.size

    def top(self):
        return self.vector.elements[self.vector.size-1]


funcs = {"+": lambda x, y: x+y, "-": lambda x, y: x-y, "*": lambda x, y: x*y}

def postfix_calc(row: str):
    stack = StackVector(100)
    number_array = []
    for item in row.split():
        if item.isdigit():
            stack.push(int(item))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.push(funcs[item](b, a))
    return stack.pop()

def main():
    row = input()
    print(postfix_calc(row))
    
if __name__ == "__main__":
    main()

