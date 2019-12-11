def process_data():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        # line is each line in the input file
        line = line.split(',')

        for entry in line:
            result.append(int(entry))
    return result

def output(n, pos):
    print('output: ', n, pos)
    return

def intcode_computer(first_input, second_input, data):
    running = True
    pos = 0
    input_seen = False
    while running:
        opcode = data[pos] % 100
        modes = data[pos] / 100
        print pos, opcode, modes, data
        if opcode == 99:
            running = False
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
            print op1, op2, result
            data[result] = op1 * op2
            pos += 4
        elif opcode == 3:
            index = data[pos + 1]
            print 'input seen?', input_seen
            if input_seen:
                print 'seen'
                data[index] = second_input
            else:
                print 'not seen'
                data[index] = first_input
                input_seen = True
            pos += 2
        elif opcode == 4:
            if modes == 0:
                index = data[pos + 1]
                op1 = data[index]
            else:
                op1 = data[pos + 1]
            output(op1, pos)
            pos += 2
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
    print 'done'
    return data

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

def challenge1():
    raw_data = process_data()
    permutations = get_permutations([0,1,2,3,4])
    max_seen = -1
    best_code = 0
    # permutations = [[4,3,2,1,0]]
    for perm in permutations:
        data = list(raw_data)
        last_input = 0
        print perm, data
        for amp in perm:
            data = intcode_computer(amp, last_input, data)
            last_input = data[0]
        if max_seen < data[0]:
            max_seen = data[0]
            best_code = perm
        max_seen = max(data[0], max_seen)
    return max_seen, best_code


print challenge1()