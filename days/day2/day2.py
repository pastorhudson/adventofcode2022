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


def run():
    total = 0
    for game in data:
        print(game[0], game[2])
        if game[2] == "X":
            total += 1
        elif game[2] == "Y":
            total += 2
        elif game[2] == "Z":
            total += 3
        match game:
            case "A X":
                total += 3
                print("Draw Rock Rock")
            case "A Z":
                print("Lose Rock Scissors")
            case "A Y":
                print("Win Rock Paper")
                total += 6

            case "B Y":
                print("Draw Paper Paper")
                total += 3
            case "B Z":
                print("Win Paper Scissors")
                total += 6
            case "B X":
                print("Lose Paper Rock")

            case "C Y":
                print("Lose Scissors Paper")

            case "C X":
                print("Win Scissors Rock")
                total += 6
            case "C Z":
                print("Draw Scissors Scissors")
                total += 3
    print(total)
    # submit(total)


if __name__ == "__main__":
    run()

