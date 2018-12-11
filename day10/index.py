def get_data():
    file = open('input.txt', 'r')
    result = []
    max_x = -100000
    max_y = -100000
    min_x = 100000
    min_y = 100000
    for line in file.readlines():
        line = line.splitlines()[0].split('<')
        p_data = line[1][:-11].split(',')
        v_data = line[2][:-1].split(',')
        (x,y) = (int(p_data[0]), int(p_data[1]))
        (vx, vy) = (int(v_data[0]), int(v_data[1]))
        result.append((x,y,vx,vy))
        if x > max_x: max_x = x
        if x < min_x: min_x = x
        if y > max_y: max_y = y
        if y < min_y: min_y = y
    return (result, (max_x-min_x, max_y-min_y))

def move_points(data):
    max_x = -100000
    min_x = 100000
    max_y = -100000
    min_y = 100000
    for i in range(len(data)):
        (x,y,vx,vy) = data[i]
        new_x = x + vx
        new_y = y + vy        
        data[i] = (new_x, new_y, vx,vy)
        if new_x > max_x: max_x = new_x
        if new_x < min_x: min_x = new_x
        if new_y > max_y: max_y = new_y
        if new_y < min_y: min_y = new_y
    return (data, max_x, min_x, max_y, min_y)

def print_board(data, max_x, min_x, max_y, min_y):
    board = []
    for _ in range(max_y - min_y + 1):
        board.append('.' * (max_x - min_x + 1))
    for item in data:
        (x,y,vx,vy) = item
        board[y-min_y] = board[y-min_y][:x-min_x] + '#' + board[y-min_y][x-min_x+1:]
    for row in board:
        print(row)
    return

def find_message():
    (data, (x_spread, y_spread)) = get_data()
    spread = x_spread
    secs = 0
    while spread > 400 or input('Proceed?') != "NO" :
        secs += 1
        (data, max_x, min_x, max_y, min_y) = move_points(data)
        spread = max_x - min_x
        if spread < 400:
            print('SECS: ', secs)
            print_board(data, max_x, min_x, max_y, min_y)
    return

find_message()