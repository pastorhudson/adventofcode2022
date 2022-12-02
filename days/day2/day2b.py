"""
Template Start
"""
from aocd.models import Puzzle
from itertools import permutations
from aocd import submit
import itertools

puzzle = Puzzle(year=2022, day=2)
data = puzzle.input_data.split("\n")

# A rock 1 - X
# B paper 2 - Y
# C scissors 3 - Z

# loss = 0
# draw = 3
# win = 6
"""
Template End
"""


def get_all_combos():

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


def run():
    total = 0
    for game in data:
        print(game[0], game[2])
        if game[2] == "X":
            total += 0
        elif game[2] == "Y":
            total += 3
        elif game[2] == "Z":
            total += 6
        print(total)
        match game:
            # X Lose
            # Y Draw
            # Z Win

            # Rock
            case "A X":  # Lose with scissors
                print(f"3 - scissors")
                total += 3
            case "A Y":  # Draw with rock
                print(f"1 - rock")
                total += 1
            case "A Z":  # Win with paper
                print(f"2 - paper")
                total += 2

            # Paper
            case "B X":  # Lose with rock
                print(f"1 - rock")
                total += 1
            case "B Z":  # Win with scissors
                total += 3
                print(f"3 - paper")

            case "B Y":  # Draw with Paper
                total += 2
                print(f"2 - paper")

            # Scissors
            case "C X":  # Lose with paper
                total += 2
                print(f"2 - paper")

            case "C Y":  # Draw with scissors
                total += 3
                print(f"3 - scissors")

            case "C Z":  # Win with rock
                total += 1
                print(f"1 - rock")

    print(total)
    # submit(total)


if __name__ == "__main__":
    run()
