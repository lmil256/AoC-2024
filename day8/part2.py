import math

def main():
    antennas = {}
    grid_width = 0
    grid_height = 0
    with open('input.txt') as infile:
        y = 0
        for line in infile:
            x = 0
            for c in line.rstrip('\n'):
                if c != '.':
                    if c in antennas:
                        antennas[c].append((y, x))
                    else:
                        antennas[c] = [(y, x)]
                x += 1
            y += 1
        grid_height = y
        grid_width = x

    antinodes = {}
    for locations in antennas.values():
        for i in range(len(locations)-1):
            for j in range(i+1, len(locations)):
                m = 0
                while True:
                    y = locations[i][0] - m*(locations[j][0] - locations[i][0])
                    x = locations[i][1] - m*(locations[j][1] - locations[i][1])
                    if -1 < y < grid_height and -1 < x < grid_width:
                        antinodes[(y, x)] = True
                    else:
                        break
                    m += 1
                m = 0
                while True:
                    y = locations[j][0] - m*(locations[i][0] - locations[j][0])
                    x = locations[j][1] - m*(locations[i][1] - locations[j][1])
                    if -1 < y < grid_height and -1 < x < grid_width:
                        antinodes[(y, x)] = True
                    else:
                        break
                    m += 1

    print(len(antinodes))

main()
