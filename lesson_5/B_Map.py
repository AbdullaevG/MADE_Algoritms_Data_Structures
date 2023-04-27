"""
B. Map
ограничение по времени на тест - 2 секунды
ограничение по памяти на тест - 256 мегабайт
ввод - стандартный ввод
вывод - стандартный вывод
Реализуйте ассоциативный массив с использованием хеш таблицы.

Входные данные
Входной файл содержит описание операций, их количество не превышает 100000.
В каждой строке находится одна из следующих операций:

    put x y — поставить в соответствие ключу x  значение y. Если ключ уже есть, то
              значение необходимо изменить.
    delete x — удалить ключ x. Если элемента x нет, то ничего делать не надо.
    get x — если ключ x есть в ассоциативном массиве, то выведите соответствующее
            ему значение, иначе выведите «none».

Ключи и значения — строки из латинских букв длинной не более 20 символов.

Выходные данные
Выведите последовательно результат выполнения всех операций get.
Следуйте формату выходного файла из примера.
Пример входных данных:
put hello privet
put bye poka
get hello
get bye
delete hello
get hello
Выход:
privet
poka
none
"""



import sys

MULTIPLIER = 29
PRIME = 100_003


class MyMap:
    def __init__(self, size):
        self.size = size
        self.PRIME = PRIME
        self.MULTIPLIER = MULTIPLIER
        self.items = [[] for _ in range(size)]

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
            if keys_values[i][0] == key:
                return index, i
        return index, None

    def put(self, key, value):
        item_index, key_index = self.is_key_in_map(key)
        if key_index is not None:
            self.items[item_index][key_index] = (key, value)
        else:
            self.items[item_index].append((key, value))

    def delete(self, key):
        item_index, key_index = indexes = self.is_key_in_map(key)
        if key_index is not None:
            self.items[item_index].pop(key_index)

    def get(self, key):
        item_index, key_index = self.is_key_in_map(key)
        if key_index is not None:
            return self.items[item_index][key_index][1]
        return "none"


def main():
    my_dict = MyMap(100_000)
    data = sys.stdin.readlines()

    for line in data:
        row = line.split()

        if row[0] == "put":
            my_dict.put(row[1], row[2])

        elif row[0] == "delete":
            my_dict.delete(row[1])

        else:
            print(my_dict.get(row[1]))


if __name__ == "__main__":
    main()
