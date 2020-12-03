#Day 1 Report Repair
#--- Day 1: Report Repair ---
# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island.
# Surely, Christmas will go on without you.
#
# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of
# a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow,
# you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
#
# To save your vacation, you need to get all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
# puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently,
# something isn't quite adding up.
#
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:

from Parser.Parser import Parser

def sum_of_three_bf(input_file):
    parser = Parser(input_file)
    input = [int(val) for val in parser.Get_Input()]
    for i in input:
        for j in input:
            for k in input:
                if i + j + k == 2020:
                    return i*j*k

#This is the answer to problem 1
def sum_of_two(input, total):
    difs = set(input)
    for val in input:
        y = total - val
        if y in difs:
            return y*val
        else:
            difs.add(y)
    raise Exception("No Sum")

def sum_of_three_smarter(input_file):
    parser = Parser(input_file)
    input = [int(val) for val in parser.Get_Input()]
    total = 2020
    for i in range(len(input)):
        x = total - input[i]
        try:
            y = sum_of_two(input[i:], x)
            return input[i]*y
        except:
            continue

if __name__ == '__main__':
    print(sum_of_three_bf(r"C:\Users\patfa\PycharmProjects\AdventOfCode\Day1\Day1P1Input"))
    print(sum_of_three_smarter(r"C:\Users\patfa\PycharmProjects\AdventOfCode\Day1\Day1P1Input"))
