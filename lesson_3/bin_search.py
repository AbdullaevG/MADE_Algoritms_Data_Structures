def bin_search(array: list, left_idx: int, right_idx: int, elem: int):
    """
    search element in the  from left index (inclusive) to right index (not inclusive)
    :param array: is sorted list
    :param: left_idx: left index of searching slice
    :param: right_idx: right index of searching slice
    :param elem: searched element
    :return: Boolean
    """


    if right_idx - left_idx == 1:
        return array[left_idx] == elem

    middle = (right_idx + left_idx)//2
    if elem == array[middle]:
        return True

    if elem < array[middle]:
        return bin_search(array, left_idx, middle, elem)
    else:
        return bin_search(array, middle, right_idx, elem)


def lower_bound(array: list, elem: int):
    """
    Find the lower bound for element in the  array from left index (inclusive) to right index (not inclusive)
    :param array: is sorted list
    :param elem: searched element
    :return: Boolean
    """
    left_idx = -1
    right_idx = len(array)

    while left_idx < right_idx - 1:
        middle = (right_idx + left_idx)//2

        if elem <= array[middle]:
            right_idx = middle
        else:
            left_idx = middle

    return right_idx



def upper_bound(array: list, elem: int):
    """
    Find the upper bound for element in the  array from left index (inclusive) to right index (not inclusive)
    :param array: is sorted list

    :param elem: searched element
    :return: Boolean
    """
    return lower_bound(array, elem+1)


def count_elements(array: list, elem: int):
    """
    Count how many times array contains elem
    :param array: array
    :param elem: element
    :return: int
    """
    return upper_bound(array, elem) - lower_bound(array, elem)


def main():
    pass


if __name__ == "__main__":
    main()


