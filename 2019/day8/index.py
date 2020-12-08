def process_data():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        for i in range(len(line)):
            result.append(int(line[i]))
    return result

def challenge1():
    data = process_data()

    width = 25
    height = 6

    index = 0

    best_layer = []
    num_zeros = width * height

    while index < len(data):
        zeroes = 0
        layer = []
        for _ in range(width * height):
            layer += [data[index]]
            if data[index] == 0:
                zeroes += 1
            index += 1

        if zeroes < num_zeros:
            best_layer = layer
            num_zeros = zeroes

    num_ones = 0
    num_twos = 0
    for num in best_layer:
        if num == 1:
            num_ones += 1
        if num == 2:
            num_twos += 1

    return num_ones * num_twos
print ('---1---')
print challenge1()

def challenge2():
    data = process_data()
    
    width = 25
    height = 6

    index = 0
    layers = []

    while index < len(data):
        layer = []
        for _ in range(width * height):
            layer += [data[index]]
            index += 1
        layers += [layer]
    
    picture = [2] * (width * height)

    pixels = []
    for i in range(width * height):
        pixels += [i]

    for layer in layers:
        for i in pixels:
            color = layer[i]
            pic_color = picture[i]
            if pic_color == 2:
                picture[i] = color

    rows = []
    for row in range(height):
        row = []
        for col in range(width):
            pix = picture.pop(0)
            if pix == 0:
                row.append('.')
            else:
                row.append('X')
        rows.append(row)
    
    for row in rows:
        print row
    

    

print('---2---')
challenge2()