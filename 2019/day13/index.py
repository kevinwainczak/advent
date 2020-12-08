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

# def challenge1():
#     data = process_data()
#     program = intcode.IntCode(data)
#     screen = []
#     while not program.halted:
#         out1 = program.run()
#         out2 = program.run()
#         out3 = program.run()
#         screen.append((out1, out2, out3))
    
#     blocks = 0
#     for element in screen:
#         if element[2] == 2:
#             blocks += 1
#     return blocks

# print(challenge1())

screen = []

def input_func():
    display = [['.'] * 44 for _ in range(20)]
    ball_col = 0
    bot_col = 0
    for element in screen:
        if element[2] == 0:
            pixel = '.'
        elif element[2] == 1:
            pixel = '|'
        elif element[2] == 2:
            pixel = '#'
        elif element[2] == 3:
            pixel = '_'
            bot_col = element[0]
        elif element[2] == 4:
            pixel = '*'
            ball_col = element[0]
        display[element[1]][element[0]] = pixel
    for row in display:
        print(row)
    if ball_col == bot_col:
        return 0
    elif ball_col < bot_col:
        return -1
    else:
        return 1
    

def challenge2():
    data = process_data()
    program = intcode.IntCode(data, input_func=input_func)
    while not program.halted:
        out1 = program.run()
        out2 = program.run()
        out3 = program.run()
        if out1 == -1 and out2 == 0:
            print('seg display: ', out3)
        screen.append((out1, out2, out3))

challenge2()

    