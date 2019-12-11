import copy

def process_data():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        # line is each line in the input file
        line = line.split(',')

        for entry in line:
            result.append(int(entry))
    return result

data = process_data()

def challenge1():
    data[1] = 12
    data[2] = 2
    running = True
    pos = 0
    while running:
        if data[pos] == 99:
            running = False
        if data[pos] == 1:
            op1 = data[pos + 1]
            op2 = data[pos + 2]
            result = data[pos + 3]
            data[result] = (data[op1] + data[op2])
        if data[pos] == 2:
            op1 = data[pos + 1]
            op2 = data[pos + 2]
            result = data[pos + 3]
            data[result] = (data[op1] * data[op2])
        pos += 4
    return data[0]


def challenge2():
    data = process_data()
    target = 19690720
    for i in range(100):
        for j in range(100):
            cdata = copy.deepcopy(data)
            cdata[1] = i
            cdata[2] = j
            running = True
            pos = 0
            while running:
                if cdata[pos] == 99:
                    running = False
                if cdata[pos] == 1:
                    op1 = cdata[pos + 1]
                    op2 = cdata[pos + 2]
                    result = cdata[pos + 3]
                    cdata[result] = (cdata[op1] + cdata[op2])
                if cdata[pos] == 2:
                    op1 = cdata[pos + 1]
                    op2 = cdata[pos + 2]
                    result = cdata[pos + 3]
                    cdata[result] = (cdata[op1] * cdata[op2])
                pos += 4
            if cdata[0] == target:
                return (i,j)
    return

print('-------- 1 --------')
print(challenge1())
print('-------- 2 --------')
print(challenge2())