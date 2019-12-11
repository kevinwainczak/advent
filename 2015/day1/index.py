import urllib.request

def get_parens():
    opener = urllib.request.build_opener()
    opener.addheaders.append(('Cookie', 'session=53616c7465645f5f979679f915a848580bba01ea0e2ed04cf63187d31932999ae9fbabca26d1cfdc36b3951649b6de85'))
    url = 'https://adventofcode.com/2015/day/1/input'
    f = opener.open(url)
    for line in f.readlines():
        # decode the line
        line = bytes.decode(line).splitlines()[0]
    return line

def process_parens():
    parens = get_parens()
    sum = 0
    for i in range(len(parens)):
        if parens[i] == '(':
            sum += 1
        else:
            sum -= 1
    return sum

def first_basement_instr():
    parens = get_parens()
    sum = 0
    for i in range(len(parens)):
        if parens[i] == '(':
            sum += 1
        else:
            sum -= 1
        if sum == -1:
            return i + 1

print(process_parens())
print(first_basement_instr())