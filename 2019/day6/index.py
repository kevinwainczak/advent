def process_orbit_map():
    orbit_map = {}
    file = open('input.txt', 'r')
    for line in file.readlines():
        entry = line.split(')')
        center = entry[0].strip()
        orbiter = entry[1].strip()

        if center in orbit_map:
            orbit_map[center] = orbit_map[center] + [orbiter]
        else:
            orbit_map[center] = [orbiter]
    return orbit_map

def challenge1():
    orbit_map = process_orbit_map()

    orbits = 0
    depth = 0
    visited = set()
    queue = []
    for planet in orbit_map['COM']:
        queue.append((planet, 1))

    while queue:
        current = queue.pop()
        curr_planet = current[0]
        depth = current[1]

        if curr_planet in orbit_map:
            for planet in orbit_map[curr_planet]:
                if planet not in visited:
                    queue.append((planet, depth + 1))
        orbits += depth

    return orbits

def process_orbit_map2():
    orbit_map = {}
    file = open('input.txt', 'r')
    for line in file.readlines():
        entry = line.split(')')
        center = entry[0].strip()
        orbiter = entry[1].strip()

        if center in orbit_map:
            orbit_map[center] = orbit_map[center] + [orbiter]
        else:
            orbit_map[center] = [orbiter]

        if orbiter in orbit_map:
            orbit_map[orbiter] = orbit_map[orbiter] + [center]
        else:
            orbit_map[orbiter] = [center]
    return orbit_map

def challenge2():
    orbit_map = process_orbit_map2()
    queue = ['SAN']
    came_from = {}
    came_from['SAN'] = None
    while queue:
        current = queue.pop()

        if current == 'YOU':
            break

        for planet in orbit_map[current]:
            if planet not in came_from:
                queue.append(planet)
                came_from[planet] = current

    current = 'YOU'
    path = []
    while current != 'SAN':
        path.append(current)
        current = came_from[current]
    path.append('SAN')

    return len(path) - 3


print('-----challenge 1------')
print(challenge1())
print('-----challenge 2------')
print(challenge2())