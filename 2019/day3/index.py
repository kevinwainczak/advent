def process_wires_get_intersections():
    seen = set()
    intersections = set()
    file = open('input.txt', 'r')
    first = False
    for line in file.readlines():
        line = line.split(',')
        x = 0
        y = 0
        first = not first
        for entry in line:
            direction = entry[0]
            dist = int(entry[1:])
            if direction == 'R':
                x_mult = 1
                y_mult = 0
            elif direction == 'L':
                x_mult = -1
                y_mult = 0
            elif direction == 'U':
                x_mult = 0
                y_mult = -1
            else:
                x_mult = 0
                y_mult = 1
            for _ in range(dist):
                x += x_mult
                y += y_mult
                if x==0 and y == 0:
                    print('******')
                if not first and str((x, y)) in seen:
                    intersections.add((x,y))
                if first:
                    seen.add(str((x, y)))
    return intersections

def challenge1():
    intersections = process_wires_get_intersections()
    result = []
    for intersection in intersections:
        result.append(abs(intersection[0]) + abs(intersection[1]))
    result = sorted(result)
    return result[0]

def challenge2():
    seen = {}
    intersections = {}
    file = open('input.txt', 'r')
    first = False
    for line in file.readlines():
        line = line.split(',')
        x = 0
        y = 0
        steps = 0
        first = not first
        for entry in line:
            direction = entry[0]
            dist = int(entry[1:])
            if direction == 'R':
                x_mult = 1
                y_mult = 0
            elif direction == 'L':
                x_mult = -1
                y_mult = 0
            elif direction == 'U':
                x_mult = 0
                y_mult = -1
            else:
                x_mult = 0
                y_mult = 1
            for _ in range(dist):
                steps += 1
                x += x_mult
                y += y_mult
                if not first and str((x, y)) in seen:
                    intersections[str((x,y))] = seen[str((x,y))] + steps
                if first:
                    seen[str((x, y))] = steps
    min_seen = 999999
    for entry in intersections:
        if intersections[entry] < min_seen:
            min_seen = intersections[entry]

    return min_seen



print(challenge1())
print(challenge2())