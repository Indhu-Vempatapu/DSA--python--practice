#remove element particularly using in-place modification 
def removeElement(nums):
  if not nums:
     return 0
  j=0
  for i in range(len(nums)):
    if nums[i]!=val:
      nums[j] = nums[i]
      j+=1
  return j
nums = list(map(int,input().split()))
print(removeElement(nums))

#Example input: nums = [3,2,2,3], val = 3
#Output: [2,2] (the remaining elements are not important so we just leave them like [2,2,_,_])
