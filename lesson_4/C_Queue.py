"""
C. Queue
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input - standard input
output - standard output
You have to implement a queue with two operations:

    "+ x" — add an element x to the queue;
    "-" — retrieve an element from the queue.
    
For each retrieval operation output the result of the operation.

Input
The first line of the input contains the number of operations — n (1≤n≤105). Next n lines contain the description
of operations one per line. The added element cannot exceed 109.

Output
Output the results of all retrieve operations in the corresponding order, one per line.

Example:
input
4
+ 1
+ 10
-
-
output
1
10
"""

import sys

CAPACITY = 10 ** 7


class Queue():
    
    def __init__(self):
        self.elements = [None] * CAPACITY
        self.begin = 0
        self.end = 1
        self.capacity = CAPACITY
        self.elements_num = 0
        
    def get_next(self, i):
        return (i + 1) % (self.capacity)
     
    def size(self):
        return (self.end + self.capacity - self.begin - 1) % (self.capacity)
    
    def push(self, item):
        if self.elements_num == self.capacity:          
            self.ensureCapacity(2)
        self.elements[self.end - 1] = item
        self.end = self.get_next(self.end)
        self.elements_num += 1
            
    def pop(self):
        pop_element = self.elements[self.begin]
        self.elements[self.begin] = None
        self.begin = self.get_next(self.begin)
        
        self.elements_num -= 1
        return pop_element
        
    def ensureCapacity(self, scaling_size):
        self.capacity *= scaling_size
        self.capacity = int(self.capacity)
        
        newElements = [None] * self.capacity
        
        s, i = self.begin, 0
        while i != self.elements_num:
            newElements[i] = self.elements[s]
            s = (s + 1) % (self.elements_num)
            i += 1
        self.end = i + 1
            
        self.elements = newElements
       
    def updateCapacity(self):
        self.ensureCapacity(scaling_size = 0.25)
            
    def is_empty(self):
        return self.size == 0
        

def main():
    queue = Queue()
    data = sys.stdin.readlines()
    m = int(data[0])
    for i in range(1, len(data)):
        if data[i][0] == "+":
            y = data[i][2:].strip()
            queue.push(y)
        else:
            print(queue.pop())
            
if __name__ == "__main__":
    main()
