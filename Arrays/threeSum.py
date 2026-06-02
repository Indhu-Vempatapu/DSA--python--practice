# Three Sum
arr = list(map(int, input().split()))
result = []
arr.sort()
for i in range(len(arr)):
  if i>0 and arr[i] == arr[i-1]:
    continue
  l, r = i+1, len(arr)-1
  while l<r:
    value = arr[i]+arr[l]+arr[r]
    if value == 0:
      result.append([arr[i],arr[l],arr[r]])
      while l<r and l[i] == l[i+1]:
        l+=1
      while l<r and r[i] == r[i-1]:
        r-=1
      l+=1
      r-=1
    elif value < 0:
      l+=1
    else:
      r-=1
print(result)

#Example Input: [-1,0,1,2,-1,-4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
