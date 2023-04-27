"""
A. Set
ограничение по времени на тест - 2 секунды
ограничение по памяти на тест - 256 мегабайт
ввод - стандартный ввод
вывод - стандартный вывод


Реализуйте множество с использованием хеш таблицы.

Входные данные
Входной файл содержит описание операций, их количество не превышает 1000000.
В каждой строке находится одна из следующих операций:

    insert x — добавить элемент x в множество. Если элемент уже есть в множестве,
               то ничего делать не надо.
    delete x — удалить элемент x. Если элемента x  нет, то ничего делать не надо.
    exists x — если ключ x  есть в множестве выведите «true», если нет «false».

В множество помещаются и извлекаются только целые числа, не превышающие по модулю 10**9.

Выходные данные
Выведите последовательно результат выполнения всех операций exists.
Следуйте формату выходного файла из примера.
"""

import sys
import random

SEPARATOR = "\n"
UNICODE = "utf-8"
A = random.randint(1, 100)
P = 10 ** 9 + 7
M = 10 ** 6 + 3


class MySet:
    def __init__(self):
        self.items = [None for _ in range(M)]
        self.rip = "rip"

    @staticmethod
    def hash_func(key):
        return ((A * key) % P) % M

    def insert(self, item):
        index = self.hash_func(item)
        rip_index = None
        rip_find = False

        while self.items[index] is not None:
            if self.items[index] == item:
                return None
            elif self.items[index] == self.rip and not rip_find:
                rip_index = index
                rip_find = True
            index = (index + 1) % M

        item_index = rip_index if rip_find else index
        self.items[item_index] = item

    def delete(self, item):
        index = self.hash_func(item)

        while self.items[index] is not None:
            if self.items[index] == item:
                self.items[index] = self.rip
                break
            index = (index + 1) % M

    def contain(self, item):
        index = self.get(item)
        if index is not None:
            return "true"
        return "false"

    def get(self, item):
        index = self.hash_func(item)

        while self.items[index] is not None:
            if self.items[index] == item:
                return index
            index = (index + 1) % M

        return None


def main():
    s = MySet()
    result = []
    data = sys.stdin.buffer.readlines()
    for i in range(len(data)):
        row = data[i].strip().decode('utf-8').split()
        command, item = row[0], int(row[1])

        if command == "insert":
            s.insert(item)

        elif command == "delete":
            s.delete(item)

        else:
            result.append(s.contain(item))
    sys.stdout.buffer.write(SEPARATOR.join(result).encode(UNICODE))


if __name__ == "__main__":
    main()