def process_data():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        # line is each line in the input file
        line = line.split()

        # add to the result array
        result.append(line[0])
    return result

data = process_data()

def challenge1():
    sum = 0
    for entry in data:
        entry = int(entry)
        entry = (entry / 3) - 2
        sum += entry
    return sum

def challenge2():
    sum = 0
    for entry in data:
        entry = int(entry)
        while entry > 0:
            entry = (entry / 3) - 2
            if entry > 0:
                sum += entry
    return sum


print(challenge1())
print(challenge2())