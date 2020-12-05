from Parser.Parser import Parser
from math import ceil, floor
import os
#x is the number of row jumps,
#y is the number of column jumps
def countTrees(input, x, y):
    trees = 0
    columns = len(input[0])
    print("Columns are: " + str(columns))
    for i in range(x, len(input), x):
        if x > y:
            if input[i][int(i/(y+1)) % (columns-1)] == '#':
                trees += 1
        else:
            if input[i][(i*y) % (columns-1)] == '#':
                trees += 1
        print(trees)
    return trees

def make_dirs_numbered(start = "C:\\Users\\patfa\\PycharmProjects\\AdventOfCode\\Day", amount=0):
    for i in range(1, amount+1):
        name = start + str(amount)
        os.mkdir(name)

def multiply_runs(input_vals: list, x: list, y: list) -> int:
    trees = 1
    if len(x) != len(y):
        return 0
    else:
        for i in range(len(x)):
            trees = trees * countTrees((input_vals), x[i], y[i])
    return trees

if __name__ == '__main__':
    parse_me = Parser(r"C:\Users\patfa\PycharmProjects\AdventOfCode\Day3\Day3P1Input")
    # problem 1
    tree_count = countTrees(parse_me.Get_Input(), 1, 3)
    print(tree_count)
    test = ['..##........',
            '#...#...#..#',
            '.#....#..#..',
            '..#.#...#.#.',
            '.#...##..#..',
            '..#.##......',
            '.#.#.#....#.',
            '.#........#.',
            '#.##...#...#',
            '#...##....##',
            '.#..#...#.#.']
    print(multiply_runs(parse_me.Get_Input(), [1, 1, 1, 1, 2], [1, 3, 5, 7, 1]))