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


def run():
    file_tree = {tuple("/"): 0}
    is_listing = False
    current_dir = []
    for line in data.splitlines():

        if "cd " in line and ".." not in line:
            current_dir.append(line.split(" ")[2])
            file_tree[tuple(current_dir)] = 0
            is_listing = False
        if "cd .." in line:
            current_dir.pop()
        if is_listing and "$" not in line:
            if "dir" in line:

                pass
            else:
                temp_dir = current_dir.copy()
                for dir in current_dir:
                    file_tree[tuple(temp_dir)] += int(line.split(" ")[0])
                    temp_dir.pop()

        elif "ls" in line:
            is_listing = True

    free_space = 70000000 - file_tree[('/',)]
    needed_space = 30000000 - free_space

    print(f"Free Space = {free_space}")
    print(f"Needed Space = {needed_space}")
    candidate_directory = None
    for directory, size in file_tree.items():
        # print(directory, size)
        if needed_space - size < 0:
            if not candidate_directory:
                candidate_directory = directory
            elif file_tree[candidate_directory] > file_tree[directory]:
                candidate_directory = directory

    print(f"Directory to delete: {'/'.join(candidate_directory)[1:]} - {file_tree[candidate_directory]} size")

    # submit(total)


run()
