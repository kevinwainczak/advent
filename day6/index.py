def get_coord_data():
    file = open('input.txt', 'r')
    x_results = []
    y_results = []
    for line in file.readlines():
        # decode the line
        line = line.splitlines()[0]
        data = line.split(' ')
        x = int(data[0][:-1])
        y = int(data[1])
        x_results.append((x,y))
        y_results.append((y,x))
    return (sorted(x_results), sorted(y_results))

def find_closest(x1,y1,coords):
    min_dist = 800
    min_coord = ''
    duplicate = False
    for coord in coords:
        (x2,y2) = coord
        man_dist = abs(x2 - x1) + abs(y2 - y1)
        if man_dist == min_dist:
            duplicate = True
        if man_dist < min_dist:
            duplicate = False
            min_dist = man_dist
            min_coord = str(x2) + ',' + str(y2)
    if duplicate:
        return ''
    else:
        return min_coord


def find_largest_area():
    (coords_by_x, coords_by_y) = get_coord_data()
    num_coords = len(coords_by_x)
    (max_x, _) = coords_by_x[num_coords - 1]
    (max_y, _) = coords_by_y[num_coords - 1]
    counts = dict()
    infinites = set()
    for x in range(max_x):
        for y in range(max_y):
            best_coord = find_closest(x,y,coords_by_x)
            if best_coord != '':
                if x == 0 or x == max_x or y == 0 or y == max_y:
                    infinites.add(best_coord)
                else:
                    if best_coord in counts:
                        counts[best_coord] += 1
                    else:
                        counts[best_coord] = 1
    max_spaces = 0
    for count in counts:
        if count not in infinites:
            if counts[count] > max_spaces:
                max_spaces = counts[count]
    return max_spaces

def get_manhattan_sums(x,y,coords, limit):
    dist_sums = 0
    for coord in coords:
        (x2,y2) = coord
        dist_sums += (abs(x2-x) + abs(y2-y))
        if dist_sums >= limit:
            return False
    return True

def get_safe_region():
    key = 10000
    (coords_by_x, coords_by_y) = get_coord_data()
    num_coords = len(coords_by_x)
    (max_x, _) = coords_by_x[num_coords -1]
    (max_y, _) = coords_by_y[num_coords -1]
    region_size = 0
    for x in range(max_x):
        for y in range(max_y):
            if get_manhattan_sums(x,y,coords_by_x, key):
                region_size += 1
    return region_size


print(find_largest_area())
print(get_safe_region())