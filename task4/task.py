import sys
def min_moves(nums):
    count = 0
    target = round(sum(nums) / len(nums))
    for num in nums:
        count += abs(num - target)
    return count
# filename = 'C:/edb/tests/task4/t.txt'
filename=sys.argv[1]
nums=[]
with open(filename, 'r') as file:
    for line in file:
        nums.append(int(line.strip()))
print(min_moves(nums))
