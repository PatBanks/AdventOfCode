from Parser.Parser import Parser


letter = ['a','b','c','d','e','f',
       'g', 'h', 'i', 'j', 'k',
       'l', 'm', 'n', 'o','p',
       'q', 'r', 's', 't', 'u',
       'v', 'w', 'x', 'y', 'z']

def get_common_yes(group):
    #gets common yes's in group
    yes = 0
    for ele in letter:
        if all(ele in item for item in group):
           yes += 1
    return yes

def find_groups(file_input):
    #Finds a list of list of groups
    groups = []
    group = []
    for person in file_input:
        if person != '\n':
            group.append(person)
        else:
            groups.append(group)
            group = []
    return groups


def get_total_answers(file_input):
    groups = find_groups(file_input)
    yes = 0
    for group in groups:
        yes = yes + get_common_yes(group)
    return yes

if __name__ == '__main__':
    parse_me = Parser(r"C:\Users\patfa\PycharmProjects\AdventOfCode\Day6\Day6Input")
    file_input = parse_me.Get_Input()
    file_input.append("\n")
    print(get_total_answers(file_input))
