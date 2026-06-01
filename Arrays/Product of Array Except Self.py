# Product of Array Except Self - using prifix and suffix approach
def productofArrayExceptSelf(lst):
  product = [1]*len(lst)
  prefix = 1
  for i in range(len(lst)):
    product[i] = prefix
    prefix *= lst[i]
  suffix = 1
  for i in range(len(lst)-1, -1, -1):
    product[i] *= suffix
    suffix *= lst[i]
  return product
lst = list(map(int, input().split()))
print(productofArrayExceptSelf(lst))

# Example Input: [2,1,3,4]
# Output: [12,24,8,6]
