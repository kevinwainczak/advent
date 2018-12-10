def get_claims_list():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        line = line.splitlines()[0]
        segments = line.split(" ")
        pos = segments[2].split(',')
        x = int(pos[0])
        y = int(pos[1][:-1])
        dims = segments[3].split('x')
        width = int(dims[0])
        height= int(dims[1])
        result.append((x,y, width, height))
    return result

def get_claims_list_with_id():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        line = line.splitlines()[0]
        segments = line.split(" ")
        ID = segments[0]
        pos = segments[2].split(',')
        x = int(pos[0])
        y = int(pos[1][:-1])
        dims = segments[3].split('x')
        width = int(dims[0])
        height= int(dims[1])
        result.append((ID, x,y, width, height))
    return result

def get_index_list(claim):
    (x, y, w, h) = claim
    results = []
    for i in range(0, w):
        for j in range(0, h):
            results.append((x+i, y+j))
    return results
    
def getAreaOfOverlaps():
    claims = get_claims_list()
    fabric = []
    for _ in range(1000):
        fabric.append([0]*1000)
    overlaps = 0
    for claim in claims:
        indices = get_index_list(claim)
        for index in indices:
            (i, j) = index
            fabric[i][j] += 1
            if fabric[i][j] == 2:
                overlaps += 1
    return overlaps

def getSafeId():
    dimension = 1000
    claims = get_claims_list_with_id()
    #claims = [("#123", 1, 3, 4, 4), ("#456", 3, 1, 4, 4), ("#789", 5, 5, 2, 2)]
    fabric = []
    for _ in range(dimension):
        fabric.append([0]*dimension)
    cells = dict()
    for claim in claims:
        (ID, x, y, w, h) = claim
        indices = get_index_list((x,y,w,h))
        cells[ID] = len(indices)
        for index in indices:
            (i,j) = index
            if fabric[i][j] == 0:
                fabric[i][j] = ID
            else:
                fabric[i][j] = 'X'
    ids = dict()
    for i in range(dimension):
        for j in range(dimension):
            if fabric[i][j] != 'X' and fabric[i][j] != 0:
                if fabric[i][j] in ids:
                    ids[fabric[i][j]] += 1
                else:
                    ids[fabric[i][j]] = 1
    for key in ids:
        if key in cells:
            if ids[key] == cells[key]:
                return key




print(getAreaOfOverlaps())
print(getSafeId())