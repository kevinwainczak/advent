def get_instrs():
    instructions = []
    with open('input.txt') as data:
        for line in data:
            instrs = line.split(' ')
            op = instrs[0]
            sign = 1 if instrs[1][0] == '+' else -1
            val = instrs[1][1:]
            instructions += [(op, sign * int(val))]
    return instructions

def p1(instructions):
    acc = 0
    index = 0
    seen_instrs = set()
    while True:
        if index in seen_instrs:
            return acc

        op = instructions[index][0]
        val = instructions[index][1]
        seen_instrs.add(index)
        if op == 'nop':
            index += 1
        elif op == 'jmp':
            index += val
        else:
            acc += val
            index += 1
        

def p2(instructions):
    flipOps = []
    for i in range(len(instructions)):
        if instructions[i][0] == 'jmp':
            flipOps += [(i, 'nop')]
        elif instructions[i][0] == 'nop':
            flipOps += [(i, 'jmp')]

    for (newIndex, newOp) in flipOps:
        acc = 0
        index = 0
        seen_instrs = set()
        while True:
            if index in seen_instrs:
                break
            if index >= len(instructions):
                return acc

            op = instructions[index][0]
            val = instructions[index][1]
            seen_instrs.add(index)

            if index == newIndex:
                op = newOp

            if op == 'nop':
                index += 1
            elif op == 'jmp':
                index += val
            else:
                acc += val
                index += 1

def main():
    instrs = get_instrs()
    print p1(instrs)
    print p2(instrs)
main()