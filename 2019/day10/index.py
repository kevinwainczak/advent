import sys

def build_map():
    asteroids = []
    file = open('input.txt', 'r')
    for line in file.readlines():
        belt = []
        line = line.strip()
        for i in range(len(line)):
            belt.append(line[i])
        asteroids += [belt]
    return asteroids

def get_all_slopes(rows, cols):
    slopes = set()
    rises_runs = set()
    for rise in range(rows):
        for run in range(cols):
            if rise == 0 and run == 0:
                continue
            if run != 0:
                slope = (rise * 1.0) / run
            else:
                slope = 'undef'
            if slope in slopes:
                continue
            slopes.add(slope)
            rises_runs.add((slope, rise, run))
            rises_runs.add((slope, -rise, run))
            rises_runs.add((slope, rise, -run))
            rises_runs.add((slope, -rise, -run))
    return rises_runs

def find_seen(rocks, row, col, slopes):
    num_seen = 0
    for (slope, rise, run) in slopes:
        y = row + rise
        x = col + run
        while x >= 0 and x < len(rocks) and y >= 0 and y < len(rocks):
            if rocks[y][x] == '#':
                num_seen += 1
                break
            x += run
            y += rise
    return num_seen

def challenge1():
    asteroids = build_map()
    slopes = get_all_slopes(len(asteroids), len(asteroids[0]))
    most_seen = 0
    for row in range(len(asteroids)):
        for col in range(len(asteroids[row])):
            if asteroids[row][col] == '.':
                continue
            seen = find_seen(asteroids, row, col, slopes)
            if seen > most_seen:
                most_seen = seen
                coords = (col, row)
    return most_seen, coords

print challenge1()

def get_all_slopes2(rows, cols):
    slopes = set()
    q1 = set()
    q2 = set()
    q3 = set()
    q4 = set()
    for rise in range(rows):
        for run in range(cols):
            if rise == 0 and run == 0:
                continue
            if run != 0:
                slope = (rise * 1.0) / run
            else:
                slope = sys.maxsize
            if slope in slopes:
                continue
            slopes.add(slope)

            if rise == 0 and run == 1:
                q1.add((0, rise, run))
                q3.add((0, rise, -run))
            elif rise == 1 and run == 0:
                q1.add((-slope, -rise, run))
                q2.add((slope, rise, run))
            else:
                q2.add((slope, rise, run))
                q1.add((-slope, -rise, run))
                q3.add((-slope, rise, -run))
                q4.add((slope, -rise, -run))
    return sorted(list(q1)), sorted(list(q2)), sorted(list(q3)), sorted(list(q4))

# (14, 17)
def challenge2():
    row = 17
    col = 14
    asteroids = build_map()
    q1, q2, q3, q4 = get_all_slopes2(len(asteroids), len(asteroids[0]))
    destroyed_asteroids = 0
    while destroyed_asteroids < 200:
        for (_, rise, run) in q1:
            x = col + run
            y = row + rise
            while x >= 0 and x < len(asteroids) and y >= 0 and y < len(asteroids):
                if asteroids[y][x] == '#':
                    destroyed_asteroids += 1
                    asteroids[y][x] == '.'
                    if destroyed_asteroids == 200:
                        return (x, y)
                    break
                x += run
                y += rise
        for (_, rise, run) in q2:
            x = col + run
            y = row + rise
            while x >= 0 and x < len(asteroids) and y >= 0 and y < len(asteroids):
                if asteroids[y][x] == '#':
                    destroyed_asteroids += 1
                    asteroids[y][x] == '.'
                    if destroyed_asteroids == 200:
                        return (x, y)
                    break
                x += run
                y += rise
        for (_, rise, run) in q3:
            x = col + run
            y = row + rise
            while x >= 0 and x < len(asteroids) and y >= 0 and y < len(asteroids):
                if asteroids[y][x] == '#':
                    destroyed_asteroids += 1
                    asteroids[y][x] == '.'
                    if destroyed_asteroids == 200:
                        return (x, y)
                    break
                x += run
                y += rise
        for (_, rise, run) in q4:
            x = col + run
            y = row + rise
            while x >= 0 and x < len(asteroids) and y >= 0 and y < len(asteroids):
                if asteroids[y][x] == '#':
                    destroyed_asteroids += 1
                    asteroids[y][x] == '.'
                    if destroyed_asteroids == 200:
                        return (x, y)
                    break
                x += run
                y += rise
    
    return (x, y)

print challenge2()