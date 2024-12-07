def main():
    grid = []
    with open('input.txt') as infile:
        for line in infile:
            grid.append(line)

    answer = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            answer += find_word(row, col, grid)
    print(answer)

def find_word(row, col, grid):
    result = 0
    target = 'XMAS'
    vecs = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1))
    if grid[row][col] != target[0]:
        return False
    for vec in vecs:
        y = row+vec[0]
        x = col+vec[1]
        found = True
        for letter in target[1:]:
            if not -1 < y < len(grid) \
                    or not -1 < x < len(grid[0]) \
                    or grid[y][x] != letter:
                found = False
                break
            y += vec[0]
            x += vec[1]
        if found:
            result += 1
    return result

main()
