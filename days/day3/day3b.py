"""
Template Start
"""
from aocd.models import Puzzle
from itertools import permutations
from aocd import submit
import itertools
from collections import Counter


puzzle = Puzzle(year=2022, day=3)
data = puzzle.input_data.split("\n")

# compartments
# Compartment 1
# Compartment 2
# lowercase item a - z = 1 - 26
# uppercase items A -Z = 27 - 52

"""
Template End
"""


def get_all_combos():
    from itertools import permutations

    # initialize lists
    list_1 = ["A", "B", "C"]
    list_2 = ["X", "Y", "Z"]

    # create empty list to store the
    # combinations
    unique_combinations = []

    # Getting all permutations of list_1
    # with length of list_2
    permut = itertools.permutations(list_1, len(list_2))

    # zip() is called to pair each permutation
    # and shorter list element into combination
    for comb in permut:
        zipped = zip(comb, list_2)
        unique_combinations.append(list(zipped))

    # printing unique_combination list
    print(unique_combinations)


def do_find_duplicates(x):
    for key, val in Counter(x).items():
        print(key, val)


def get_letter_value(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26


def run():
    total = 0
    for sack1, sack2, sack3 in zip(*[iter(data)]*3):
        print(sack1)
        print(sack2)
        print(sack3)

        unique = list(set(sack1).intersection(set(sack2)).intersection(set(sack3)))[0]
        letter_value = get_letter_value(unique)
        print(f"{unique} = {letter_value}\n")
        total += letter_value
        # print("\n")
    print(total)
    # submit(total)


if __name__ == "__main__":
    run()

