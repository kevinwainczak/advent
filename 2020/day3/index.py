def makeLand():
    result = []
    with open('input.txt') as data:
        for line in data:
            line = line.strip()
            result += [line]
    return result

def isTree(grid, row, col):
    return grid[row][col % len(grid[row])] == '#'

def main():
    grid = makeLand()
    result = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for (dCol, dRow) in slopes:
        row = 0
        col = 0
        trees = 0
        while row < len(grid):
            if isTree(grid, row, col):
                trees += 1
            row += dRow
            col += dCol
        result = result * trees
    return result

print main()