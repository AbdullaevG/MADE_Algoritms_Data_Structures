def test(algorithm):

    array_1 = [1, -1, 1, -1, 1, -1]
    result_1 = algorithm(array_1)
    if result_1 == [-1, -1, -1, 1, 1, 1]:
        print("test#1___ok!")
    else:
        print("test#1___fail")
        print("Correct_result: ", [-1, -1, -1, 1, 1, 1])
        print("Algorithm output: ", result_1)

    array_2 = [10, 9, 8, 10, 9, 8]
    result_2 = algorithm(array_2)
    if result_2 == [8, 8, 9, 9, 10, 10]:
        print("test#2___ok!")
    else:
        print("test#2___fail")
        print("Correct_result: ", [8, 8, 9, 9, 10, 10])
        print("Algorithm output: ", result_2)


    array_3 = [0, 0, -1, -1]
    result_3 = algorithm(array_3)
    if result_3 == [-1, -1, 0, 0]:
        print("test#3___ok!")
    else:
        print("test#3___fail")
        print("Correct_result: ", [-1, -1, 0, 0])
        print("Algorithm output: ", result_3)

    array_4 = [2]
    result_4 = algorithm(array_4)
    if result_4 == [2]:
        print("test#4___ok!")
    else:
        print("test#4___fail")
        print("Correct_result: ", [2])
        print("Algorithm output: ", result_4)