
from Parser.Parser import Parser
import unittest
import re

byr = None
iyr = None
eyr = None
hgt = None
hcl = None
ecl = None
pid = None

must_have = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]

def valid_number(num, lt, gt):
    if lt <= num <= gt:
        print(str(num) + " is valid")
        return True
    else:
        print(str(num) + " is invalid")
        return False

def valid_byr(byr):
    return valid_number(int(byr), 1920, 2002)

def valid_iyr(iyr):
    return valid_number(int(iyr), 2010, 2020)

def valid_eyr(eyr):
    return valid_number(int(eyr), 2020, 2030)

def valid_hgt(hgt):
    if hgt[-2:] == 'cm':
        try:
            return valid_number(int(hgt[0:-2]), 150, 193)
        except:
            return False
    elif hgt[-2:] == 'in':
        try:
            return valid_number(int(hgt[0:-2]), 59, 76)
        except:
            print(str(hgt) + " is invalid")
            return False
    else:
        print(str(hgt) + " is invalid")
        return False

def valid_hcl(hcl):
    pattern = r"#[a-f0-9]{6,6}$"
    match = re.match(pattern, hcl)
    if match:
        print(str(hcl) + " is valid")
        return True
    else:
        print(str(hcl) + " is invalid")
        return False

def valid_ecl(ecl):
    match = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for val in match:
        if val == ecl:
            print(str(ecl) + " is valid")
            return True
    print(str(ecl) + " is invalid")
    return False

def valid_pid(pid):
    pattern = r"[0-9]{9,9}$"
    match = re.match(pattern, pid)
    if match:
        print(str(pid) + " is valid")
        return True
    else:
        print(str(pid) + " is invalid")
        return False

validate = {"byr": valid_byr,
            "iyr": valid_iyr,
            "eyr": valid_eyr,
            "hgt": valid_hgt,
            "hcl": valid_hcl,
            "ecl": valid_ecl,
            "pid": valid_pid,
            }

def getPassports(passport_batch):
    parse_me = Parser(passport_batch)
    file_input = parse_me.Get_Input()
    file_input.append("\n")
    passports = []
    key = ""
    for value in file_input:
        if value != "\n":
            key = key + value
        else:
            passports.append(key)
            key = ""
    return passports

def countValidPassports(criteria: list, passports: list):
    valid_passports = 0
    for value in passports:
        invalid = False
        value = value.split()
        print(value)
        check_contains = []
        isValid = []
        for val in value:
            val1 = val.split(':')[0]
            check_contains.append(val1)
            val2 = val.split(':')[1]
            for item in criteria:
                if val1 in item:
                    print("item: " + str(item))
                    isValid.append(validate[val1](val2))
        if not all(item in check_contains for item in criteria):
               isValid.append(False)

        print("status is: " + str(isValid))
        if False in isValid:
            continue
        else:
            valid_passports += 1
    return(valid_passports)



if __name__ == '__main__':
    passport_batch = r"C:\Users\patfa\PycharmProjects\AdventOfCode\Day4\Day4P1Input"
    passports = getPassports(passport_batch)
    print(passports)
    valid = countValidPassports(must_have, passports)
    print(valid)

    # test = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n",
    #         "byr:1937 iyr:2017 cid:147 hgt:183cm\n",
    #         "\n",
    #         "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n",
    #         "hcl:#cfa07d byr:1929\n",
    #         "\n",
    #         "hcl:#ae17e1 iyr:2013\n",
    #         "eyr:2024\n",
    #         "ecl:brn pid:760753108 byr:1931\n",
    #         "hgt:179cm\n",
    #         "\n",
    #         "hcl:#cfa07d eyr:2025 pid:166559648",
    #         "iyr:2011 ecl:brn hgt:59in\n"]

    # passports = []
    # key = ""
    # test.append("\n")
    # for value in test:
    #     if value != "\n":
    #         value = value.split()
    #         for val in value:
    #             key = key + val.split(':')[0] + " "
    #     else:
    #         passports.append(key)
    #         key = ""
    # for passport in passports:
    #     print(passport.split())

    #print(passports)
    #vt = countValidPassports(must_have, passports)
    #print(vt)