def roman_to_arab(roman = "MCMXCIX"):

    adding_rule = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    div_rule = {("I", "V"): 3, ("I", "X"): 8,
                ("X", "L"): 30, ("X", "C"): 80,
                ("C", "D"): 300, ("C", "M"): 800,
                }

    arabic = 0
    prev_literal = None

    for literal in roman:
        if prev_literal and adding_rule[prev_literal] < adding_rule[literal]:
            arabic += div_rule[(prev_literal, literal)]
        else:
            arabic += adding_rule[literal]
        prev_literal = literal

    return arabic

def test_roman_to_arab():

    roman_1 = "MCMXCIX"
    assert roman_to_arab(roman_1) == 1999

    roman_2 = "MCML"
    assert roman_to_arab(roman_2) == 1950

    roman_3 = "MCMLXXXVIII"
    assert roman_to_arab(roman_3) == 1988

test_roman_to_arab()


def arab_to_roman(arab):

    num_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
               (50, "L"), (40, "XV"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    roman = ""
    for item in num_map:
        num, literal = item
        while arab >= num:
            roman += literal
            arab -= num

    return roman


def test_arab_to_roman():

    roman_1 = "MCMXCIX"
    assert arab_to_roman(1999) == roman_1

    roman_2 = "MCML"
    assert arab_to_roman(1950) == roman_2

    roman_3 = "MCMLXXXVIII"
    assert arab_to_roman(1988) == roman_3


test_arab_to_roman()

def sort_kings(names: list):
    for i, name in enumerate(names):
        name_order = name.split()
        name, order = name_order

        arab_order = str(roman_to_arab(order))
        name = name + " " + arab_order

        names[i] = name

    names.sort()
    for name_order in names:
        name_order = name_order.split()

        name, arab_order = name_order
        print(name + " " + arab_to_roman(int(arab_order)))



def sort_kings_simple(names: list):
    names = [name.split() for name in names]
    names.sort(key = lambda x: roman_to_arab(x[1]))
    names.sort(key = lambda x: x[0])
    for name in names:
        print(*name)

sort_kings(['Philip I', 'Philippe II', "Louis IX", "Louis VIII"])

#n = int(input())
#inp_list = []
#for i in range(n):
#    king = input()
#    inp_list.append(king)
#sort_kings(inp_list)
