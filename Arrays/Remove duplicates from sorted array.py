#remove duplicates from sorted array using two pointers technique and in-place modification 
def removeDuplicatesFromSortedArray(arr):
  if not arr:
    return 0
  i = 0
  for j in range(1,len(arr)):
    if arr[j] !=arr[i]:
      i+=1
      arr[i]=arr[j]
  return i+1
arr = list(map(int, input().split()))
print(removeDuplicatesFromSortedArray(arr))

#Example Input : [1,2,2,3,4,4,5]
#Output: [1,2,3,4,5]
