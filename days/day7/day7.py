"""
Template Start
"""
from pprint import pprint

from aocd.models import Puzzle
from itertools import permutations
from aocd import submit
import itertools
from collections import Counter

puzzle = Puzzle(year=2022, day=7)
data = puzzle.input_data
"""
Template End
"""


def run():
    file_tree = {tuple("/"): 0}
    is_listing = False
    current_dir = []
    parent_dir = []
    for line in data.splitlines():

        if "cd " in line and ".." not in line:
            # file_tree[line.split(" ")[2]] = {}
            print(line.split(" ")[2])
            current_dir.append(line.split(" ")[2])
            file_tree[tuple(current_dir)] = 0
            is_listing = False
        if "cd .." in line:
            current_dir.pop()
        if is_listing and "$" not in line:
            if "dir" not in line:
                temp_dir = current_dir.copy()
                for dir in current_dir:
                    file_tree[tuple(temp_dir)] += int(line.split(" ")[0])
                    temp_dir.pop()

        elif "ls" in line:
            is_listing = True
        else:
            print(f"{tuple(current_dir)} is current dir")

    pprint(file_tree)
    total = 0
    for directory, size in file_tree.items():
        if size <= 100000:
            total += size

    print(total)
    # submit(total)


run()
