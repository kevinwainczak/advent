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
    print('output', n, pos)
    return

def challenge1():
    data = process_data()
    running = True
    pos = 0
    while running:
    # for _ in range(15):
        opcode = data[pos] % 100
        modes = data[pos] / 100
        # print (pos, opcode, modes, data[:15])
        if opcode == 99:
            running = False
        elif opcode == 1:
            result = data[pos + 3]
            # print result
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
            # print op1, op2
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
            data[result] = op1 * op2
            pos += 4
        elif opcode == 3:
            index = data[pos + 1]
            data[index] = 1
            pos += 2
        elif opcode == 4:
            if modes == 0:
                index = data[pos + 1]
                op1 = data[index]
            else:
                op1 = data[pos + 1]
            output(op1, pos)
            pos += 2
    return data[0]

# print(challenge1())

def challenge2():
    data = process_data()
    running = True
    pos = 0
    while running:
    # for _ in range(15):
        opcode = data[pos] % 100
        modes = data[pos] / 100
        # print (pos, opcode, modes, data[:15])
        if opcode == 99:
            running = False
        elif opcode == 1:
            result = data[pos + 3]
            # print result
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
            # print op1, op2
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
            data[result] = op1 * op2
            pos += 4
        elif opcode == 3:
            index = data[pos + 1]
            data[index] = 5
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
    return data[0]

print(challenge2())