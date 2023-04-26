"""
Implement a data structure that supports three operations:
   push 𝑥 — add an element 𝑥;
   extract-min — extract the minimal element;
   decrease-key 𝑖𝑑 𝑣 — decrease an element to 𝑣  added by previous operation 𝑖𝑑
 
If you are asked to decrease an element that was already extracted then you should do nothing.
All operations are enumerated starting from 1

Input
The input file contains performed operations, one per line. Arguments of push and decrease-key 
operations do not exceed 109  by an absolute value.

It is guaranteed that for any "decrease-key id v" the operation with identifier 𝑖𝑑  is push operation.

Output
For each operation extract-min output two integers on a separate line: the value of the element and the identifier 
of push operation that added it. If there are several minimal elements, output any of them. If the data structure is empty, output "*".
"""

import sys


INF_ELEMENT = 10 ** 9 + 1
INF_ORDER = 10 ** 9 + 1


class Node():
    def __init__(self, order, value):
        self.order = order
        self.value = value


class Heap():
    def __init__(self):
        self.elements = []
        self.size = 0
        
    
    def insert(self, item):
        self.elements.append(item)
        item_index = self.size
        self.size += 1
        self.shift_up(index = item_index)
        
    
    def shift_up(self, index):
        i = index   # Переобозначение, для того чтобы далее строки не были слишком длинными ))
        
        while (i > 0) and self.elements[i].value < self.elements[(i - 1) // 2].value:
            self.elements[i], self.elements[(i - 1) // 2] = self.elements[(i - 1) // 2], self.elements[i]
            i = (i - 1) // 2
            
    
    def extract_min(self):
        if self.size == 0:
            return ["*"]
        
        temp_min = self.elements[0]
        self.elements[0], self.elements[self.size - 1] = self.elements[self.size - 1], self.elements[0]
        self.elements.pop()
        self.size -= 1
        self.shift_down(index = 0)
        
        return [temp_min.value, temp_min.order]
    
    
    def shift_down(self, index):
        i = index   # Переобозначение, для того чтобы далее строки не были слишком длинными ))
        while 2 * i + 1 < self.size:
            cur = self.elements[i]
            left = self.elements[2 * i + 1]
            
            if 2 * i + 2 == self.size:
                right = Node(INF_ORDER, INF_ELEMENT)
            else:
                right = self.elements[2 * i + 2]
            
            
            if left.value < right.value and left.value < cur.value:
                self.elements[2 * i + 1], self.elements[i] = self.elements[i], self.elements[2 * i + 1]
                i = 2 * i + 1
            
            elif right.value < cur.value:
                self.elements[2 * i + 2], self.elements[i] = self.elements[i], self.elements[2 * i + 2]
                i = 2 * i + 2
            
            else:
                break
                    
    
    def change_value(self, order, new_value):
        index = 0
        
        while self.elements[index].order != order and index < self.size:
            index += 1
        
        if index == self.size:
            return
        
        self.elements[index].value = new_value
        self.shift_up(index = index)
        self.shift_down(index = index)


def main():
    
    heap = Heap()            
    data  = sys.stdin.readlines()
    order = 1

    for item in data:
        item = item.split()
        
        if item[0] == "push":
            heap.insert(Node(order, int(item[1])))
            order += 1
            
        elif item[0] == "extract-min":
            print(*heap.extract_min())
            order += 1
            
        else:
            changing_item_order = int(item[1])
            heap.change_value(changing_item_order, int(item[2]))
            order += 1
            
if __name__ == "__main__":
    main()
