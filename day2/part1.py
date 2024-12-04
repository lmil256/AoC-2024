reports = []
with open('input.txt') as infile:
    for line in infile:
        reports.append([int(x) for x in line.split(' ')])
        
answer = 0
for report in reports:
    is_safe = True
    prev_diff = 0
    for prev, curr in zip(report[:-1], report[1:]):
        diff = curr-prev
        if diff*prev_diff < 0 or not (1 <= abs(diff) <= 3):
            is_safe = False
            break
        prev_diff = diff
    if is_safe:
        answer += 1

print(answer)
