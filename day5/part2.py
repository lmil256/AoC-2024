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
        answer += sort(update, rules)

    print(answer)

def sort(update, rules):
    valid = True
    for i in range(1, len(update)):
        if update[i] not in rules:
            continue
        correct_pos = i
        for j in range(i-1, -1, -1):
            if update[j] in rules[update[i]]:
                valid = False
                correct_pos = j
        if correct_pos != i:
            update.insert(correct_pos, update.pop(i))

    return update[len(update)//2] if not valid else 0

main()
