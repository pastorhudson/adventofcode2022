"""
Template Start
"""
from aocd.models import Puzzle
from itertools import permutations
from aocd import submit
import itertools
from collections import Counter

puzzle = Puzzle(year=2022, day=5)
data = puzzle.input_data.split("\n")[10:]

"""
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
"""




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
    final = []
    column1 = ["C", "Q", 'B']
    column1.reverse()

    column2 = ["Z", "W", "Q", "R"]
    column2.reverse()

    column3 = ["V", "L", "R", "M", "B"]
    column3.reverse()

    column4 = ["W", "T", "V", "H", "Z", "C"]
    column4.reverse()

    column5 = ["G", "V", "N", "B", "H", "Z", "D"]
    column5.reverse()

    column6 = ["Q", "V", "F", "J", "C", "P", "N", "H"]
    column6.reverse()

    column7 = ["S", "Z", "W", "R", "T", "G", "D"]
    column7.reverse()

    column8 = ["P", "Z", "W", "B", "N", "M", "G", "C"]
    column8.reverse()

    column9 = ["P", "F", "Q", "W", "M", "B", "J", "N"]
    column9.reverse()
    big_list = [column1, column2, column3, column4, column5, column6, column7, column8, column9]
    print(big_list)

    for items in data:
        print(items)

        crates_to_move = int(items.split(" ")[1])
        from_stack = int(items.split(" ")[3]) - 1
        to_stack = int(items.split(" ")[5]) - 1
        print(crates_to_move, from_stack, to_stack)

        for operations in range(crates_to_move):
            big_list[to_stack].append(big_list[from_stack].pop())
    for stack in big_list:
        print(stack[-1])

    # submit(total)


if __name__ == "__main__":
    run()

