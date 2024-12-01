list1 = []
list2 = []
with open('input.txt') as infile:
    for line in infile:
        nums = line.split('  ')
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

list1.sort()
list2.sort()
answer = 0
for num1, num2 in zip(list1, list2):
    answer += abs(num1-num2)

print(answer)
