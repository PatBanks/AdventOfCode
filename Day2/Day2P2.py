# --- Part Two ---
# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate
# Authentication System is expecting.
#
# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the
# sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.
#
# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second
# character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these
# positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy
# enforcement.
#
# Given the same example list from above:
#
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

from Parser.Parser import Parser

def valid_passwords():
    parse_me = Parser(r"C:\Users\patfa\PycharmProjects\AdventOfCode\Day2P1Input")
    valid_count = 0
    for line in parse_me.Get_Input():
        values = line.split()
        pos1 = int(values[0].split('-')[0])-1
        pos2 = int(values[0].split('-')[1])-1
        key = values[1][0]
        password = values[-1]
        if pos2 < len(password) and pos1 < len(password):
            if password[pos1] == key:
                if password[pos2] == key:
                    print("invalid")
                else:
                    valid_count +=1
                    print("invalid")
            elif password[pos2] == key:
                valid_count +=1
            else:
                print("invalid")
        elif pos2 < len(password):
            if password[pos2] == key:
                valid_count +=1
            else:
                print("invalid")
        elif pos1 < len(password):
            if password[pos1] == key:
                valid_count += 1
            else:
                print("invalid")
        else:
            print("invalid")
    return valid_count

if __name__ == '__main__':
    print(valid_passwords())