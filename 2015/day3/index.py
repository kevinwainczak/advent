import urllib.request

def get_dir_data():
    opener = urllib.request.build_opener()
    opener.addheaders.append(('Cookie', 'session=53616c7465645f5f979679f915a848580bba01ea0e2ed04cf63187d31932999ae9fbabca26d1cfdc36b3951649b6de85'))
    url = 'https://adventofcode.com/2015/day/3/input'
    f = opener.open(url)
    data = []
    for line in f.readlines():
        # decode the line
        line = bytes.decode(line).splitlines()[0]
    return line

def find_dup_houses():
    dirs = get_dir_data()
    visited = {'0,0': 1}
    x_axis = 0
    y_axis = 0
    for i in range(len(dirs)):
        if dirs[i] == '<':
            x_axis -= 1
        elif dirs[i] == '>':
            x_axis += 1
        elif dirs[i] == '^':
            y_axis += 1
        else:
            y_axis -= 1
        loc = str(x_axis) + ',' + str(y_axis)
        if loc in visited:
            visited[loc] += 1
        else:
            visited[loc] = 1
    total_houses = 0
    for key in visited:
        total_houses += 1
    return total_houses

def find_robo_houses():
    dirs = get_dir_data()
    visited = {'0,0': 1}
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0
    i = 0
    while i < len(dirs):
        if dirs[i] == '<': santa_x -= 1
        elif dirs[i] == '>': santa_x += 1
        elif dirs[i] == '^': santa_y += 1
        else: santa_y -= 1
        if dirs[i+1] == '<': robo_x -= 1
        elif dirs[i+1] == '>': robo_x += 1
        elif dirs[i+1] == '^': robo_y += 1
        else: robo_y -= 1
        santa_loc = str(santa_x) + ',' + str(santa_y)
        robo_loc = str(robo_x) + ',' + str(robo_y)
        if santa_loc in visited: visited[santa_loc] += 1
        else: visited[santa_loc] = 1
        if robo_loc in visited: visited[robo_loc] += 1
        else: visited[robo_loc] = 1
        i += 2
    total_houses = 0
    for key in visited:
        total_houses += 1
    return total_houses


print(find_dup_houses())
print(find_robo_houses())

