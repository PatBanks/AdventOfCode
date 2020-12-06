from Parser.Parser import Parser




if __name__ == '__main__':
    parse_me = Parser(r"C:\Users\patfa\PycharmProjects\AdventOfCode\Day6\Day6Input")
    plane_answers = parse_me.Get_Input()
    plane_answers.append("\n")
    print(plane_answers)
    group_answers = []
    g = ""
    unique = 0
    for answers in plane_answers:
        if answers != "\n":
            g = g + answers.strip()
            continue
        if g != "" and answers == "\n":
            group_answers.append(g)
            g = ""
    for answer in group_answers:
        unique = unique + len(set(answer))
    print(unique)

    print(group_answers)
