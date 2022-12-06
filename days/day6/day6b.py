"""
Template Start
"""
from aocd.models import Puzzle
from itertools import permutations
from aocd import submit
import itertools
from collections import Counter

puzzle = Puzzle(year=2022, day=6)
data = puzzle.input_data



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
    for index, letter in enumerate(data):
        if len(data[index:index + 14]) == len(set(data[index:index + 14])):
            print(index + 14)
            break

    # submit(total)


if __name__ == "__main__":
    run()

