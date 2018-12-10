def make_freq_list():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        line = line.splitlines()[0]
        operator = line[0]
        number = int(line[1:])
        if operator == "-":
            result.append(number * -1)
        else:
            result.append(number)
    return result

def getNetFrequency():
    freqs = make_freq_list()
    sum = 0
    for n in freqs:
        sum += n
    return sum

def getFirstDuplicateFrequency():
    freqs = make_freq_list()
    seenFreqs = {0}
    repeatFreqFound = False
    sum = 0
    index = 0
    while (not repeatFreqFound):
        sum += freqs[index % len(freqs)]
        if sum in seenFreqs:
            return sum
        seenFreqs.add(sum)
        index += 1
    return


print(getNetFrequency())
print(getFirstDuplicateFrequency())