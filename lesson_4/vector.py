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