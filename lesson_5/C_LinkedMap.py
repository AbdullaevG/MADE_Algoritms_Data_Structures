import sys

SEPARATOR = "\n"
UNICODE = "utf-8"
MULTIPLIER = 31
PRIME = 100_003
SHIFT = 96


class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class MyMap:
    def __init__(self, size):
        self.size = size
        self.PRIME = 100_003
        self.MULTIPLIER = 29
        self.items = [[] for _ in range(size)]
        self.prev_added = None

    @staticmethod
    def shift_ord(letter):
        return ord(letter) - ord("a") - 1

    def hash_func(self, string: str):
        result = 0
        for letter in string:
            result = (result * self.MULTIPLIER + self.shift_ord(letter)) % self.PRIME
        return result % self.size

    def is_key_in_map(self, key):
        index = self.hash_func(key)
        keys_values = self.items[index]
        values_num = len(keys_values)

        for i in range(values_num):
            if keys_values[i].key == key:
                return index, i
        return index, None

    def put(self, key, value):
        item_index, key_index = self.is_key_in_map(key)

        if key_index is not None:
            self.items[item_index][key_index].value = value

        else:
            item = Node(key, value)
            self.items[item_index].append(item)
            if self.prev_added:
                self.prev_added.next = item
                item.prev = self.prev_added
            self.prev_added = self.items[item_index][-1]

    def delete(self, key):
        item_index, key_index = self.is_key_in_map(key)

        if key_index is not None:
            deleted_item = self.items[item_index][key_index]
            prev_item, next_item = deleted_item.prev, deleted_item.next

            if prev_item:
                prev_item.next = next_item
                if deleted_item == self.prev_added:
                    self.prev_added = self.prev_added.prev

            if next_item:
                next_item.prev = prev_item

            self.items[item_index].pop(key_index)
            if prev_item is None and next_item is None:
                self.prev_added = None

    def get(self, key):
        item_index, key_index = self.is_key_in_map(key)
        if key_index is not None:
            return self.items[item_index][key_index].value
        return "none"

    def prev_or_next(self, key, next_flag=False):
        item_index, key_index = self.is_key_in_map(key)

        if key_index is not None:
            item = self.items[item_index][key_index]
            prev = item.prev
            next = item.next

            if next_flag:
                if next:
                    return next.value

            elif prev:
                return prev.value

            return "none"

        return "none"

    def prev(self, key):
        return self.prev_or_next(key, next_flag=False)

    def next_(self, key):
        return self.prev_or_next(key, next_flag=True)


def main():
    m = MyMap(100_000)
    results = []
    data = sys.stdin.readlines()

    for raw in data:
        raw = raw.split()

        if raw[0] == "put":
            m.put(raw[1], raw[2])

        elif raw[0] == "delete":
            m.delete(raw[1])

        elif raw[0] == "prev":
            results.append(m.prev(raw[1]))

        elif raw[0] == "next":
            results.append(m.next_(raw[1]))

        else:
            results.append(m.get(raw[1]))

    sys.stdout.buffer.write(SEPARATOR.join(results).encode(UNICODE))


if __name__ == "__main__":
    main()