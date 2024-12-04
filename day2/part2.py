def main():
    reports = []
    with open('input.txt') as infile:
        for line in infile:
            reports.append([int(x) for x in line.split(' ')])
            
    answer = 0
    for report in reports:
        if is_safe(report):
            answer += 1
        else:
            for i in range(len(report)):
                new_report = [x for x in report]
                del new_report[i]
                if is_safe(new_report):
                    answer += 1
                    break

    print(answer)

def is_safe(report):
    prev_diff = 0
    for prev, curr in zip(report[:-1], report[1:]):
        diff = curr-prev
        if diff*prev_diff < 0 or not (1 <= abs(diff) <= 3):
            return False
        prev_diff = diff

    return True

main()
