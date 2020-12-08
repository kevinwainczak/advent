def intcode(data, phase_setting, input_signal):
    running = True
    phase_setting_used = False
    pos = 0
    output = -1

    while running:
        opcode = data[pos] % 100
        modes = data[pos] / 100
        
        # OPCODE 99
        if opcode == 99:
            running = False

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

            if not phase_setting_used:
                data[index] = phase_setting
                phase_setting_used = True
            else:
                data[index] = input_signal

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
    return output