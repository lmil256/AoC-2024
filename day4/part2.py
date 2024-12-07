def main():
    grid = []
    with open('input.txt') as infile:
        for line in infile:
            grid.append(line)

    answer = 0
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            if find_cross(row, col, grid):
                answer += 1

    print(answer)

def find_cross(row, col, grid):
    if grid[row][col] != 'A':
        return False
    nw = grid[row-1][col-1]
    ne = grid[row-1][col+1]
    sw = grid[row+1][col-1]
    se = grid[row+1][col+1]
    return nw in 'MS' and se in 'MS' and nw != se \
            and ne in 'MS' and sw in 'MS' and ne != sw

main()
