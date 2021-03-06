def get(data, pos):
    if pos >= len(data):
        data += [0] * (pos - len(data) + 1)
    return data[pos]

def assign(data, pos, val):
    if pos >= len(data):
        data += [0] * (pos - len(data) + 2)
    data[pos] = val

def intcode(data, input_signals, pos):
    running = True
    phase_setting_used = False
    relative_base = 0

    while running:
        opcode = get(data,pos) % 100
        modes = get(data,pos) / 100
        
        # OPCODE 99
        if opcode == 99:
            return
        # OPCODE 1 - ADD
        elif opcode == 1:
            if modes % 10 == 0:
                index = get(data, pos + 1)
                op1 = get(data, index)
            elif modes % 10 == 1:
                op1 = get(data, pos + 1)
            else:
                index = get(data, pos + 1) + relative_base
                op1 = get(data, index)
            if (modes / 10) % 10 == 0:
                index = get(data, pos + 2)
                op2 = get(data, index)
            elif (modes / 10) % 10 == 1:
                op2 = get(data, pos + 2)
            else:
                index = get(data, pos + 2) + relative_base
                op2 = get(data, index)
            if modes / 100 == 0:
                result = get(data,pos + 3)
            else:
                result = get(data, pos + 3) + relative_base
            assign(data, result, op1 + op2)
            pos += 4

        # OPCODE 2 - MULTIPLY
        elif opcode == 2:
            if modes % 10 == 0:
                index = get(data, pos + 1)
                op1 = get(data, index)
            elif modes % 10 == 1: 
                op1 = get(data, pos + 1)
            else:
                index = get(data, pos + 1) + relative_base
                op1 = get(data, index)
            if (modes / 10) % 10 == 0:
                index = get(data, pos + 2)
                op2 = get(data, index)
            elif (modes / 10) % 10 == 1:
                op2 = get(data, pos + 2)
            else:
                index = get(data, pos + 2) + relative_base
                op2 = get(data, index)
            if modes / 100 == 0:
                result = get(data, pos + 3)
            else:
                result = get(data, pos + 3) + relative_base
        
            assign(data, result, op1 * op2)
            pos += 4

        # OPCODE 3 - INPUT VAL SWAP
        elif opcode == 3:
            if modes == 0:
                index = get(data, pos + 1)
            else:
                index = get(data, pos + 1) + relative_base

            # if len(input_signals) == 0:
            #     return 'go', list([data, [], pos]), output
            assign(data, index, input_signals[0])

            pos += 2

        # OPCODE 4 - OUTPUT
        elif opcode == 4:
            if modes == 0:
                index = get(data, pos + 1)
                op1 = get(data, index)
            elif modes == 1:
                op1 = get(data, pos + 1)
            else:
                index = get(data, pos + 1) + relative_base
                op1 = get(data, index)
            print op1
            pos += 2

        # OPCODE 5 - JUMP IF TRUE
        elif opcode == 5:
            if modes % 10 == 0:
                index = get(data, pos + 1)
                op1 = get(data, index)
            elif modes % 10 == 1:
                op1 = get(data, pos + 1)
            else:
                index = get(data, pos + 1) + relative_base
                op1 = get(data, index)
            if modes / 10 == 0:
                index = get(data, pos + 2)
                op2 = get(data, index)
            elif modes / 10 == 1:
                op2 = get(data, pos + 2)
            else:
                index = get(data, pos + 2) + relative_base
                op2 = get(data, index)
            if op1 != 0:
                pos = op2
            else:
                pos += 3

        # OPCODE 6 - JUMP IF FALSE
        elif opcode == 6:
            if modes % 10 == 0:
                index = get(data, pos + 1)
                op1 = get(data, index)
            elif modes % 10 == 1:
                op1 = get(data, pos + 1)
            else:
                index = get(data, pos + 1) + relative_base
                op1 = get(data, index)
            if modes / 10 == 0:
                index = get(data, pos + 2)
                op2 = get(data, index)
            elif modes / 10 == 1:
                op2 = get(data, pos + 2)
            else:
                index = get(data, pos + 2) + relative_base
                op2 = get(data, index)
            if op1 == 0:
                pos = op2
            else:
                pos += 3

        # OPCODE 7 - LESS THAN
        elif opcode == 7:
            if modes % 10 == 0:
                index = get(data, pos + 1)
                op1 = get(data, index)
            elif modes % 10 == 1:
                op1 = get(data, pos + 1)
            else:
                index = get(data, pos + 1) + relative_base
                op1 = get(data, index)
            if (modes / 10) % 10 == 0:
                index = get(data, pos + 2)
                op2 = get(data, index)
            elif (modes / 10) % 10 == 1:
                op2 = get(data, pos + 2)
            else:
                index = get(data, pos + 2) + relative_base
                op2 = get(data, index)
            if modes / 100 == 0:
                result = get(data, pos + 3)
            else:
                result = get(data, pos + 3) + relative_base
            if op1 < op2:
                assign(data, result, 1)
            else:
                assign(data, result, 0)
            pos += 4

        # OPCODE 8 - EQUALS
        elif opcode == 8:
            if modes % 10 == 0:
                index = get(data, pos + 1)
                op1 = get(data, index)
            elif modes % 10 == 1:
                op1 = get(data, pos + 1)
            else:
                index = get(data, pos + 1) + relative_base
                op1 = get(data, index)
            if (modes / 10) % 10 == 0:
                index = get(data, pos + 2)
                op2 = get(data, index)
            elif (modes / 10) % 10 == 1:
                op2 = get(data, pos + 2)
            else:
                index = get(data, pos + 2) + relative_base
                op2 = get(data, index)
            if modes / 100 == 0:
                result = get(data, pos + 3)
            else:
                result = get(data, pos + 3) + relative_base
            if op1 == op2:
                assign(data, result, 1)
            else:
                assign(data, result, 0)
            pos += 4
        
        #OPCODE 9 - RELATIVE BASE ADJUSTMENT
        elif opcode == 9:
            if modes == 0:
                index = get(data, pos + 1)
                op1 = get(data, index)
            elif modes == 1:
                op1 = get(data, pos + 1)
            elif modes == 2:
                index = relative_base + get(data, pos + 1)
                op1 = get(data, index)
            relative_base += op1

            pos += 2
    # RETURN RESULT
    print('should never get here')
    return output

def process_data():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        # line is each line in the input file
        line = line.split(',')

        for entry in line:
            result.append(int(entry))
    return result

def challenge1():
    data = process_data()
    intcode(data, [2], 0)

challenge1()