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

def run():
    total = 0
    for items in data:
        first_pair = items.split(",")[0].split("-")
        second_pair = items.split(",")[1].split("-")
        """
        2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8
        """
        if int(first_pair[0]) <= int(second_pair[0]) and int(first_pair[1]) >= int(second_pair[1]):
            # print(f"First Pair {first_pair} Second Pair {second_pair}")
            total += 1
        elif int(second_pair[0]) <= int(first_pair[0]) and int(second_pair[1]) >= int(first_pair[1]):
            # print(f"First Pair {first_pair} Second Pair {second_pair}")
            total += 1

    print(total)
    # submit(total)


if __name__ == "__main__":
    run()

