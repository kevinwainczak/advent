from math import floor

grid_serial_num = 6303

def create_power_grid():
    grid = []
    for y in range(0, 300):
        grid.append([0] * 300)
        for x in range(0,300):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += grid_serial_num
            power_level *= rack_id
            if power_level < 100:
                power_level = -5
            else:
                power_level = (floor(power_level / 100) % 10) - 5
            grid[y][x-1] = power_level
    return grid

def get_best_square():
    grid = create_power_grid()
    best_sum = -10000000
    best_coords = (-1, -1)
    for y in range(0, 297):
        row1 = grid[y]
        row2 = grid[y+1]
        row3 = grid[y+3]
        for x in range(0, 297):
            sum = 0
            sum += row1[x] + row1[x+1] + row1[x+2]
            sum += row2[x] + row2[x+1] + row2[x+2]
            sum += row3[x] + row3[x+1] + row3[x+2]
            if sum > best_sum:
                best_sum = sum
                best_coords = (x+1, y+1)
    return (best_sum, best_coords)

def sum_grid(grid):
    new_grid = []
    for _ in range(300):
        new_grid.append([0] * 300)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if x == 0 and y == 0:
                new_grid[y][x] = grid[y][x]
            elif x == 0 and y != 0:
                new_grid[y][x] = new_grid[y-1][x] + grid[y][x]
            elif y == 0 and x != 0:
                new_grid[y][x] = new_grid[y][x-1] + grid[y][x]
            else:
                new_grid[y][x] = new_grid[y][x-1] + new_grid[y-1][x] - new_grid[y-1][x-1] + grid[y][x]
    return new_grid
                
            
def get_best_any():
    grid = create_power_grid()
    grid = sum_grid(grid)
    best_sum = -5 * 300
    best_coords = (-1, -1)
    best_i = -1
    for i in range(1, 301):
        for y in range(i-1, 300):
            for x in range(i-1, 300):
                if x == i-1 and y == i-1:
                    sum = grid[y][x]
                elif x == i-1 and y != i-1:
                    sum = grid[y][x] - grid[y-i][x]
                elif x != i-1 and y == i-1:
                    sum = grid[y][x] - grid[y][x-i]
                else:
                    sum = grid[y][x] - grid[y][x-i] - grid[y-i][x] + grid[y-i][x-i]
                if sum > best_sum:
                    best_sum = sum
                    best_coords = (x+2-i,y+1-i)
                    best_i = i
    return (best_i, best_sum, best_coords)

print(get_best_any())
print(get_best_square())

