import intcode
def process_data():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        # line is each line in the input file
        line = line.split(',')

        for entry in line:
            result.append(int(entry))
    return result

def get_permutations(numbers):
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return [[numbers[0]]]
    perms = []
    for perm in get_permutations(numbers[1:]):
        for i in range(len(perm) + 1):
            perms.append(perm[:i] + [numbers[0]] + perm[i:])
    return perms

# def challenge1():
#     raw_data = process_data()
#     permutations = get_permutations([0,1,2,3,4])
#     max_seen = -1
#     for permutation in permutations:
#         input_signal = 0
#         for phase_setting in permutation:
#             data = list(raw_data)
#             input_signal = intcode.intcode(data, phase_setting, input_signal)

#         if max_seen < input_signal:
#             max_seen = input_signal
#             best_code = permutation

#     return max_seen, best_code

# print('---1---')
# print challenge1()

def intcode(data, input_signals, pos):
    running = True
    phase_setting_used = False
    output = -1

    while running:
        opcode = data[pos] % 100
        modes = data[pos] / 100
        
        # OPCODE 99
        if opcode == 99:
            return 'halt', list(), output

        # OPCODE 1 - ADD
        elif opcode == 1:
            result = data[pos + 3]
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            else:
                op1 = data[pos + 1]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            else:
                op2 = data[pos + 2]
            data[result] = (op1 + op2)
            pos += 4

        # OPCODE 2 - MULTIPLY
        elif opcode == 2:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            else: 
                op1 = data[pos + 1]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            else:
                op2 = data[pos + 2]
            result = data[pos + 3]
            data[result] = op1 * op2
            pos += 4

        # OPCODE 3 - INPUT VAL SWAP
        elif opcode == 3:
            index = data[pos + 1]

            if len(input_signals) == 0:
                return 'go', list([data, [], pos]), output
            data[index] = input_signals.pop(0)

            pos += 2

        # OPCODE 4 - OUTPUT
        elif opcode == 4:
            if modes == 0:
                index = data[pos + 1]
                op1 = data[index]
            else:
                op1 = data[pos + 1]
            output = op1
            pos += 2

        # OPCODE 5 - JUMP IF TRUE
        elif opcode == 5:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            else:
                op1 = data[pos + 1]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            else:
                op2 = data[pos + 2]
            if op1 != 0:
                pos = op2
            else:
                pos += 3

        # OPCODE 6 - JUMP IF FALSE
        elif opcode == 6:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            else:
                op1 = data[pos + 1]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            else:
                op2 = data[pos + 2]
            if op1 == 0:
                pos = op2
            else:
                pos += 3

        # OPCODE 7 - LESS THAN
        elif opcode == 7:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            else:
                op1 = data[pos + 1]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            else:
                op2 = data[pos + 2]
            result = data[pos + 3]
            if op1 < op2:
                data[result] = 1
            else:
                data[result] = 0
            pos += 4

        # OPCODE 8 - EQUALS
        elif opcode == 8:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            else:
                op1 = data[pos + 1]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            else:
                op2 = data[pos + 2]
            result = data[pos + 3]
            if op1 == op2:
                data[result] = 1
            else:
                data[result] = 0
            pos += 4
    
    # RETURN RESULT
    print('should never get here')
    return output

def challenge2():
    data = process_data()
    permutations = get_permutations([5,6,7,8,9])
    max_seen = -1
    for permutation in permutations:
        states = [
            [list(data), list([permutation[0]]), 0], #a
            [list(data), list([permutation[1]]), 0], #b
            [list(data), list([permutation[2]]), 0], #c
            [list(data), list([permutation[3]]), 0], #d
            [list(data), list([permutation[4]]), 0], #e
        ]
        status = 'go'
        amp = 0
        output = 0

        while not (status == 'halt' and amp == 0):
            input_data = states[amp][0]
            states[amp][1].append(output)
            input_signals = states[amp][1]
            pos = states[amp][2]
            status, state, output = intcode(input_data, input_signals, pos)
            states[amp] = state
            amp = (amp + 1) % 5
        
        if output > max_seen:
            max_seen = output
            best_code = permutation

    print (max_seen, best_code)

        
    

print('---2---')
challenge2()



def get(data, pos):
    if pos >= len(data):
        data.append([0] * (pos - len(data)))
        return 0
    else:
        return data[pos]

def intcode(data, input_signals, pos):
    running = True
    phase_setting_used = False
    output = -1
    relative_base = 0

    while running:
        opcode = data[pos] % 100
        modes = data[pos] / 100
        
        # OPCODE 99
        if opcode == 99:
            return 'halt', list(), output

        # OPCODE 1 - ADD
        elif opcode == 1:
            result = data[pos + 3]
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            elif modes % 10 == 1:
                op1 = data[pos + 1]
            else:
                index = data[pos + 1] + relative_base
                op1 = data[index]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            elif modes / 10 == 1:
                op2 = data[pos + 2]
            else:
                index = data[pos + 2] + relative_base
                op2 = data[index]
            data[result] = (op1 + op2)
            pos += 4

        # OPCODE 2 - MULTIPLY
        elif opcode == 2:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            elif modes % 10 == 1: 
                op1 = data[pos + 1]
            else:
                index = data[pos + 1] + relative_base
                op1 = data[index]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            elif modes / 10 == 1:
                op2 = data[pos + 2]
            else:
                index = data[pos + 2] + relative_base
                op2 = data[index]
            result = data[pos + 3]
            data[result] = op1 * op2
            pos += 4

        # OPCODE 3 - INPUT VAL SWAP
        elif opcode == 3:
            if modes == 0:
                index = data[pos + 1]
            else:
                index = data[pos + 1] + relative_base

            if len(input_signals) == 0:
                return 'go', list([data, [], pos]), output
            data[index] = input_signals.pop(0)

            pos += 2

        # OPCODE 4 - OUTPUT
        elif opcode == 4:
            if modes == 0:
                index = data[pos + 1]
                op1 = data[index]
            elif modes == 1:
                op1 = data[pos + 1]
            else:
                index = data[pos + 1] + relative_base
                op1 = data[index]
            output = op1
            pos += 2

        # OPCODE 5 - JUMP IF TRUE
        elif opcode == 5:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            elif modes % 10 == 1:
                op1 = data[pos + 1]
            else:
                index = data[pos + 1] + relative_base
                op1 = data[index]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            elif modes / 10 == 1:
                op2 = data[pos + 2]
            else:
                index = data[pos + 2] + relative_base
                op2 = data[index]
            if op1 != 0:
                pos = op2
            else:
                pos += 3

        # OPCODE 6 - JUMP IF FALSE
        elif opcode == 6:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            elif modes % 10 == 1:
                op1 = data[pos + 1]
            else:
                index = data[pos + 1] + relative_base
                op1 = data[index]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            elif modes / 10 == 1:
                op2 = data[pos + 2]
            else:
                index = data[pos + 2] + relative_base
                op2 = data[index]
            if op1 == 0:
                pos = op2
            else:
                pos += 3

        # OPCODE 7 - LESS THAN
        elif opcode == 7:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            elif modes % 10 == 1:
                op1 = data[pos + 1]
            else:
                index = data[pos + 1] + relative_base
                op1 = data[index]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            elif modes / 10 == 1:
                op2 = data[pos + 2]
            else:
                index = data[pos + 2] + relative_base
                op2 = data[index]
            result = data[pos + 3]
            if op1 < op2:
                data[result] = 1
            else:
                data[result] = 0
            pos += 4

        # OPCODE 8 - EQUALS
        elif opcode == 8:
            if modes % 10 == 0:
                index = data[pos + 1]
                op1 = data[index]
            elif modes % 10 == 1:
                op1 = data[pos + 1]
            else:
                index = data[pos + 2]
                op1 = data[index]
            if modes / 10 == 0:
                index = data[pos + 2]
                op2 = data[index]
            elif modes / 10 == 1:
                op2 = data[pos + 2]
            else:
                index = data[pos + 2]
                op2 = data[index]
            result = data[pos + 3]
            if op1 == op2:
                data[result] = 1
            else:
                data[result] = 0
            pos += 4
        
        #OPCODE 9 - RELATIVE BASE ADJUSTMENT
        elif opcode == 9:
            if modes == 0:
                index = data[pos + 1]
                op1 = data[index]
            elif modes == 1:
                op1 = data[pos + 1]
            elif modes == 2:
                index = relative_base + data[pos + 1]
                op1 = data[index]
            relative_base += op1

            pos += 2
    # RETURN RESULT
    print('should never get here')
    return output