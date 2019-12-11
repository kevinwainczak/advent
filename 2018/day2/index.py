import urllib.request

def get_box_id_list():
    opener = urllib.request.build_opener()
    opener.addheaders.append(('Cookie', 'session=53616c7465645f5f979679f915a848580bba01ea0e2ed04cf63187d31932999ae9fbabca26d1cfdc36b3951649b6de85'))
    url = 'https://adventofcode.com/2018/day/2/input'
    f = opener.open(url)
    result = []
    for line in f.readlines():
        line = bytes.decode(line).splitlines()[0]
        result.append(line)
    return result

def string_to_freq_map(s):
    freq = dict()
    sorted(s)
    for c in s:
        if not c in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    return freq

def repeatLetterIndicator(entry):
    twoRepeat = 0
    threeRepeat = 0
    for key in entry:
        if entry[key] == 2:
            twoRepeat = 1
        elif entry[key] == 3:
            threeRepeat = 1
    return (twoRepeat, threeRepeat)
    


def produceChecksum():
    box_ids = get_box_id_list()
    freq_maps = list(map(string_to_freq_map, box_ids))
    numTwoRepeats = 0
    numThreeRepeats = 0
    for entry in freq_maps:
        (twoRepeats, threeRepeats) = repeatLetterIndicator(entry)
        numTwoRepeats += twoRepeats
        numThreeRepeats += threeRepeats
    return numTwoRepeats * numThreeRepeats
    
def findOffByOneIds(ids):
    for id1 in ids:
        for id2 in ids:
            numDifferent = 0
            for i in range(0, len(id1)):
                if id1[i] != id2[i]:
                    numDifferent += 1
                if numDifferent == 2:
                    break
            if numDifferent == 1:
                return (id1, id2)

def closestStrings():
    box_ids = get_box_id_list()
    (id1, id2) = findOffByOneIds(box_ids)
    print(id1, id2)
    result = ""
    for i in range(0, len(id1)):
        if id1[i] == id2[i]:
            result += id1[i]
    return result
    

print(produceChecksum())
print(closestStrings())