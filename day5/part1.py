def main():
    rules = {}
    updates = []
    with open('input.txt') as infile:
        # Read the order rules
        while True:
            line = infile.readline().rstrip('\n')
            if line == '':
                break
            nums = [int(x) for x in line.split('|')]
            if nums[0] in rules:
                rules[nums[0]].append(nums[1])
            else:
                rules[nums[0]] = [nums[1]]

        # Read the updates
        while True:
            line = infile.readline().rstrip('\n')
            if line == '':
                break
            updates.append([int(x) for x in line.split(',')])

    answer = 0
    for update in updates:
        if is_valid(update, rules):
            answer += update[len(update)//2]

    print(answer)

def is_valid(update, rules):
    for i in range(1, len(update)):
        if update[i] not in rules:
            continue
        for prev in update[i-1::-1]:
            if prev in rules[update[i]]:
                return False

    return True

main()
