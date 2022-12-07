"""
Template Start
"""
from aocd.models import Puzzle
from itertools import permutations
from aocd import submit
import itertools
from collections import Counter

puzzle = Puzzle(year=2022, day=4)
data = puzzle.input_data.split("\n")

# print(data)

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
        first_start, first_end = items.split(",")[0].split("-")
        second_start, second_end = items.split(",")[1].split("-")
        print(first_start)
        print(first_end)
        """
        2-4,6-8 # no overlap first_start < second start & first end is less than second end
        2-3,4-5 # no overlap first start < second start & first end is less than second end
        5-7,7-9 # yes overlap because second_end = first_start
        2-8,3-7 # yes overlap second start is greater than first start and less than second end
        6-6,4-6 # yes first start is greater than second start and less than second end
        2-6,4-8 # yes first start is less than second start
        """
        if int(second_start) >= int(first_start) and int(second_start) <= int(first_end):
            # print(f"First Pair {first_pair} Second Pair {second_pair}")
            total += 1
        elif int(first_start) >= int(second_start) and int(first_start) <= int(second_end):
        #     # print(f"First Pair {first_pair} Second Pair {second_pair}")
            total += 1

    print(total)
    # submit(total)


if __name__ == "__main__":
    run()

