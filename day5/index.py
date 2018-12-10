def get_polymer_data():
    file = open('input.txt', 'r')
    for line in file.readlines():
        # decode the line
        line = line.splitlines()[0]
    return line
        
def does_cancel(x,y):
    return abs(ord(x)-ord(y)) == 32

def react_polymer(polymer):
    reaction_happened = True
    while reaction_happened:
        reaction_happened = False
        i = 1
        while i < len(polymer):
            # check backwards for reaction
            if does_cancel(polymer[i-1], polymer[i]):
                reaction_happened = True
                polymer = polymer[:i-1] + polymer[i+1:]
            else:
                i += 1
    return polymer

def process_polymer():
    polymer = get_polymer_data()
    return len(react_polymer(polymer))

def remove_instances(poly, x,y):
    temp = poly
    temp = temp.replace(x, '')
    temp = temp.replace(y, '')
    return temp


def get_shortest_polymer():
    polymer = get_polymer_data()
    results = []
    for n in range(65, 65+26):
        print('Processing ' + chr(n))
        temp_poly = remove_instances(polymer, chr(n), chr(n+32))
        temp_poly = react_polymer(temp_poly)
        print(chr(n) + ' is of length ' + str(len(temp_poly)))
        results += len(temp_poly)
    return min(results)


print(process_polymer())
get_shortest_polymer()