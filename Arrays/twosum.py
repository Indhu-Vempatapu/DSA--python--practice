def twoSum(nums, target):
  seen = {}
  for i, num in enumerate(nums):
    diff = traget - num
    if diff in seen:
      return [seen[diff], i]
    seen[num] = i
  return 
nums = list(map(int, input().split()))
target = int(input())
print(twoSum(nums, target))
