list1 = []
list2 = []
with open('input.txt') as infile:
    for line in infile:
        nums = line.split('  ')
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

answer = 0
for num in list1:
    answer += num*list2.count(num)

print(answer)
