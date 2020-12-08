# def get(data, pos):
#     if pos >= len(data):
#         data += [0] * (pos - len(data) + 1)
#     return data[pos]

# def assign(data, pos, val):
#     if pos >= len(data):
#         data += [0] * (pos - len(data) + 2)
#     data[pos] = val

# def intcode(data, input_signal, pos):
#     running = True
#     phase_setting_used = False
#     relative_base = 0
#     outputs = []

#     while running:
#         opcode = get(data,pos) % 100
#         modes = get(data,pos) / 100
        
#         # OPCODE 99
#         if opcode == 99:
#             return list(('halt', data, outputs, pos))
#         # OPCODE 1 - ADD
#         elif opcode == 1:
#             if modes % 10 == 0:
#                 index = get(data, pos + 1)
#                 op1 = get(data, index)
#             elif modes % 10 == 1:
#                 op1 = get(data, pos + 1)
#             else:
#                 index = get(data, pos + 1) + relative_base
#                 op1 = get(data, index)
#             if (modes / 10) % 10 == 0:
#                 index = get(data, pos + 2)
#                 op2 = get(data, index)
#             elif (modes / 10) % 10 == 1:
#                 op2 = get(data, pos + 2)
#             else:
#                 index = get(data, pos + 2) + relative_base
#                 op2 = get(data, index)
#             if modes / 100 == 0:
#                 result = get(data,pos + 3)
#             else:
#                 result = get(data, pos + 3) + relative_base
#             assign(data, result, op1 + op2)
#             pos += 4

#         # OPCODE 2 - MULTIPLY
#         elif opcode == 2:
#             if modes % 10 == 0:
#                 index = get(data, pos + 1)
#                 op1 = get(data, index)
#             elif modes % 10 == 1: 
#                 op1 = get(data, pos + 1)
#             else:
#                 index = get(data, pos + 1) + relative_base
#                 op1 = get(data, index)
#             if (modes / 10) % 10 == 0:
#                 index = get(data, pos + 2)
#                 op2 = get(data, index)
#             elif (modes / 10) % 10 == 1:
#                 op2 = get(data, pos + 2)
#             else:
#                 index = get(data, pos + 2) + relative_base
#                 op2 = get(data, index)
#             if modes / 100 == 0:
#                 result = get(data, pos + 3)
#             else:
#                 result = get(data, pos + 3) + relative_base
        
#             assign(data, result, op1 * op2)
#             pos += 4

#         # OPCODE 3 - INPUT VAL SWAP
#         elif opcode == 3:
#             if modes == 0:
#                 index = get(data, pos + 1)
#             else:
#                 index = get(data, pos + 1) + relative_base

#             # if len(input_signals) == 0:
#             #     return 'go', list([data, [], pos]), output
#             assign(data, index, input_signal)

#             pos += 2

#         # OPCODE 4 - OUTPUT
#         elif opcode == 4:
#             if modes == 0:
#                 index = get(data, pos + 1)
#                 op1 = get(data, index)
#             elif modes == 1:
#                 op1 = get(data, pos + 1)
#             else:
#                 index = get(data, pos + 1) + relative_base
#                 op1 = get(data, index)
#             outputs += [op1]
#             if len(outputs) == 2:
#                 return list(('go', data, outputs, pos))
#             pos += 2

#         # OPCODE 5 - JUMP IF TRUE
#         elif opcode == 5:
#             if modes % 10 == 0:
#                 index = get(data, pos + 1)
#                 op1 = get(data, index)
#             elif modes % 10 == 1:
#                 op1 = get(data, pos + 1)
#             else:
#                 index = get(data, pos + 1) + relative_base
#                 op1 = get(data, index)
#             if modes / 10 == 0:
#                 index = get(data, pos + 2)
#                 op2 = get(data, index)
#             elif modes / 10 == 1:
#                 op2 = get(data, pos + 2)
#             else:
#                 index = get(data, pos + 2) + relative_base
#                 op2 = get(data, index)
#             if op1 != 0:
#                 pos = op2
#             else:
#                 pos += 3

#         # OPCODE 6 - JUMP IF FALSE
#         elif opcode == 6:
#             if modes % 10 == 0:
#                 index = get(data, pos + 1)
#                 op1 = get(data, index)
#             elif modes % 10 == 1:
#                 op1 = get(data, pos + 1)
#             else:
#                 index = get(data, pos + 1) + relative_base
#                 op1 = get(data, index)
#             if modes / 10 == 0:
#                 index = get(data, pos + 2)
#                 op2 = get(data, index)
#             elif modes / 10 == 1:
#                 op2 = get(data, pos + 2)
#             else:
#                 index = get(data, pos + 2) + relative_base
#                 op2 = get(data, index)
#             if op1 == 0:
#                 pos = op2
#             else:
#                 pos += 3

#         # OPCODE 7 - LESS THAN
#         elif opcode == 7:
#             if modes % 10 == 0:
#                 index = get(data, pos + 1)
#                 op1 = get(data, index)
#             elif modes % 10 == 1:
#                 op1 = get(data, pos + 1)
#             else:
#                 index = get(data, pos + 1) + relative_base
#                 op1 = get(data, index)
#             if (modes / 10) % 10 == 0:
#                 index = get(data, pos + 2)
#                 op2 = get(data, index)
#             elif (modes / 10) % 10 == 1:
#                 op2 = get(data, pos + 2)
#             else:
#                 index = get(data, pos + 2) + relative_base
#                 op2 = get(data, index)
#             if modes / 100 == 0:
#                 result = get(data, pos + 3)
#             else:
#                 result = get(data, pos + 3) + relative_base
#             if op1 < op2:
#                 assign(data, result, 1)
#             else:
#                 assign(data, result, 0)
#             pos += 4

#         # OPCODE 8 - EQUALS
#         elif opcode == 8:
#             if modes % 10 == 0:
#                 index = get(data, pos + 1)
#                 op1 = get(data, index)
#             elif modes % 10 == 1:
#                 op1 = get(data, pos + 1)
#             else:
#                 index = get(data, pos + 1) + relative_base
#                 op1 = get(data, index)
#             if (modes / 10) % 10 == 0:
#                 index = get(data, pos + 2)
#                 op2 = get(data, index)
#             elif (modes / 10) % 10 == 1:
#                 op2 = get(data, pos + 2)
#             else:
#                 index = get(data, pos + 2) + relative_base
#                 op2 = get(data, index)
#             if modes / 100 == 0:
#                 result = get(data, pos + 3)
#             else:
#                 result = get(data, pos + 3) + relative_base
#             if op1 == op2:
#                 assign(data, result, 1)
#             else:
#                 assign(data, result, 0)
#             pos += 4
        
#         #OPCODE 9 - RELATIVE BASE ADJUSTMENT
#         elif opcode == 9:
#             if modes == 0:
#                 index = get(data, pos + 1)
#                 op1 = get(data, index)
#             elif modes == 1:
#                 op1 = get(data, pos + 1)
#             elif modes == 2:
#                 index = relative_base + get(data, pos + 1)
#                 op1 = get(data, index)
#             relative_base += op1

#             pos += 2
#     # RETURN RESULT
#     print('should never get here')
#     return output

# def process_data():
#     file = open('input.txt', 'r')
#     result = []
#     for line in file.readlines():
#         # line is each line in the input file
#         line = line.split(',')

#         for entry in line:
#             result.append(int(entry))
#     return result

# def challenge1():
#     data = process_data()
#     status = 'go'
#     input_sig = 0
#     pos = 0

#     x = 0
#     y = 0
#     dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
#     dir_index = 0
#     panels = dict()
#     while status == 'go':
#         status, data, output, pos = intcode(data, input_sig, pos)
#         print status, output, pos
#         if status == 'go':
#             # get outputs
#             color = output[0]
#             direction = output[1]

#             # paint panel
#             panels[(x,y)] = color

#             # rotate
#             if direction == 0:
#                 dir_index = (dir_index - 1 + 4) % 4
#             else:
#                 dir_index = (dir_index + 1 + 4) % 4
            
#             # move
#             x += dirs[dir_index][0]
#             y += dirs[dir_index][1]

#             # determine next input sig
#             input_sig = panels.get((x,y), 0)
#     return len(panels)

# print challenge1()
    
import sys, intcode

def paint_execute(code, initial_color):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    program = intcode.IntCode(code)
    x = y = direction = 0
    panel = { (x, y): initial_color }
    while not program.halted:
        program.input(panel[(x, y)] if (x, y) in panel else 0)
        output1 = program.run()
        output2 = program.run()
        if not program.halted:
            panel[(x, y)] = output1
            direction = ((direction + 1) if output2 == 1 else (direction - 1 + len(directions))) % len(directions)
            x, y = x + directions[direction][0], y + directions[direction][1]
    return panel

def build_registration(panel_points):
    registration = [[' ']*40 for _ in range(6)]
    for row in range(6):
        for col in range(40):
            if panel_points.get((col, row), 0) == 1:
                registration[row][col] = '*'
    return '\n'.join(''.join(row) for row in registration)

code = list(map(int, open(sys.argv[1]).read().split(',')))

part1 = len(paint_execute(code, 0))
part2 = build_registration(paint_execute(code, 1))

print('Part 1: {0}, Part 2: \n{1}'.format(part1, part2))