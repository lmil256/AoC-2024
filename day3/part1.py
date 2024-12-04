import re

def main():
    expr = re.compile(r'mul\((\d+),(\d+)\)')
    answer = 0
    with open('input.txt') as infile:
        for line in infile:
            for pair in expr.findall(line):
                answer += int(pair[0])*int(pair[1])
    print(answer)

main()
