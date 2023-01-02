
def get_count_list(word: str):
    count_list = [0 for _ in range(26)]
    a_code = ord("a")
    for letter in word:
        count_list[ord(letter) - a_code] += 1

    return count_list


def is_anogramms(word_1: str, word_2: str):
    word_1 = word_1.lower()
    word_2 = word_2.lower()

    return get_count_list(word_1) == get_count_list(word_2)


print(is_anogramms("radzhab", "baradzh"))
print(is_anogramms("tazhib", "bizhat"))
print(is_anogramms("karim", "mikarr"))