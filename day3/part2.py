import re

def main():
    expr = re.compile(r'(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)')
    answer = 0
    with open('input.txt') as infile:
        active = True
        for line in infile:
            pos = 0
            while True:
                m = expr.search(line, pos)
                #pdb.set_trace()
                if m is None:
                    break
                if active:
                    if m.group(1) is not None:
                        pass
                    elif m.group(2) is not None:
                        active = False
                    else:
                        answer += int(m.group(3))*int(m.group(4))
                elif m.group(1) is not None:
                    active = True
                pos = m.end()

    print(answer)

main()
