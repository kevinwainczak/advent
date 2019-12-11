import urllib.request

def get_box_data():
    opener = urllib.request.build_opener()
    opener.addheaders.append(('Cookie', 'session=53616c7465645f5f979679f915a848580bba01ea0e2ed04cf63187d31932999ae9fbabca26d1cfdc36b3951649b6de85'))
    url = 'https://adventofcode.com/2015/day/2/input'
    f = opener.open(url)
    data = []
    for line in f.readlines():
        # decode the line
        line = bytes.decode(line).splitlines()[0]
        dims = line.split('x')
        l = int(dims[0])
        w = int(dims[1])
        h = int(dims[2])
        data.append((l,w,h))
    return data

def get_total_paper():
    boxes = get_box_data()
    sum = 0
    for box in boxes:
        (l,w,h) = box
        side1 = l*w
        side2 = w*h
        side3 = h*l
        sum += (2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3))
    return sum

def get_ribbon_len():
    boxes = get_box_data()
    sum = 0
    for box in boxes:
        (l,w,h) = box
        sorted_box = sorted([l,w,h])
        sum += 2*sorted_box[0] + 2*sorted_box[1]
        sum += l*w*h
    return sum

print(get_total_paper())
print(get_ribbon_len())