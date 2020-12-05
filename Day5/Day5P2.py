# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.
#
# It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's
# a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing
# from your list as well.
#
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
#
# What is the ID of your seat?


from Parser.Parser import Parser
from math import ceil
from math import floor

def convert_to_binary(columns, rows):
    binary_columns = ""
    binary_rows = ""
    for i in columns:
        if i == 'F':
            binary_columns = binary_columns + "0"
        elif i == 'B':
            binary_columns = binary_columns + "1"
    for i in rows:
        if i == 'R':
            binary_rows += "1"
        elif i == 'L':
            binary_rows += "0"
    binary_columns = int(binary_columns, base=2)
    binary_rows = int(binary_rows, base=2)
    return binary_columns * 8 + binary_rows


def max_seat_number(file_input):
    max_seat_id = 0
    seat_numbers = []
    for line in file_input:
        columns = line[0:7]
        rows = line[7:10]
        new = convert_to_binary(columns, rows)
        seat_numbers.append(new)
        if max_seat_id < new:
            max_seat_id = new
    return max_seat_id, seat_numbers

def get_missing_seat(seat_numbers):
    for i in range(1, len(seat_numbers)):
        if seat_numbers[i] != (seat_numbers[i-1] + 1):
            return seat_numbers[i-1] + 1

if __name__ == '__main__':
    parse_me = Parser(r"C:\Users\patfa\PycharmProjects\AdventOfCode\Day5\Day5P1")
    seats = parse_me.Get_Input()
    seats = [seat.strip() for seat in seats]
    msn, seat_numbers = max_seat_number(seats)
    seat_numbers.sort()
    print(get_missing_seat(seat_numbers))
