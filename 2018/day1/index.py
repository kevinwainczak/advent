import urllib.request

def make_freq_list():
    opener = urllib.request.build_opener()
    opener.addheaders.append(('Cookie', 'session=53616c7465645f5f979679f915a848580bba01ea0e2ed04cf63187d31932999ae9fbabca26d1cfdc36b3951649b6de85'))
    url = 'https://adventofcode.com/2018/day/1/input'
    f = opener.open(url)
    result = []
    for line in f.readlines():
        line = bytes.decode(line).splitlines()[0]
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