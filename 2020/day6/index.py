def p1():
    with open('input.txt') as data:
        result = 0
        yes_answers = set()
        for line in data:
            if line == '\n':
                result += len(yes_answers)
                yes_answers = set()
            else:
                yes_answers.update(set(line.strip()))
        return result

def p2():
    with open('input.txt') as data:
        result = 0
        yes_answers = set()
        next_line_new_group = True
        for line in data:
            if line == '\n':
                result += len(yes_answers)
                yes_answers = set()
                next_line_new_group = True
            else:
                if next_line_new_group:
                    yes_answers = set(line.strip())
                    next_line_new_group = False
                else:
                    yes_answers = yes_answers.intersection(set(line.strip()))
        return result

# print p1()
print p2()