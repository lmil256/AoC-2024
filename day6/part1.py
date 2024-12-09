def main():
    grid = []
    with open('input.txt') as infile:
        for line in infile:
            grid.append(line.rstrip('\n'))

    visited = {}
    y_pos = -1
    x_pos = -1
    dy = -1
    dx = 0
    for i in range(len(grid)):
        try:
            x_pos = grid[i].index('^')
            y_pos = i
            break
        except ValueError:
            pass

    while -1 < y_pos+dy < len(grid) and -1 < x_pos+dx < len(grid[0]):
        if grid[y_pos+dy][x_pos+dx] != '#':
            y_pos += dy
            x_pos += dx
            visited[(y_pos, x_pos)] = True
        else:
            # Turn right
            dy, dx = dx, -dy

    print(len(visited))

main()
