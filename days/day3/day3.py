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


def run():
    total = 0
    for items in data:

        first_compartment = items[0:len(items)//2]
        second_compartment = items[len(items)//2 if len(items)%2 == 0
                                        else ((len(items)//2)+1):]

        # printing result
        print(f"The first part of string : {set(first_compartment)}")
        print(f"The second part of string : {set(second_compartment)}")
        unique = list(set(first_compartment).intersection(set(second_compartment)))[0]
        if unique.islower():
            unique = ord(unique) - 96
            print(unique)
            total += unique
        else:
            unique = ord(unique) - 64 + 26
            print(unique)
            total += unique
    print(total)
    submit(total)


if __name__ == "__main__":
    run()

