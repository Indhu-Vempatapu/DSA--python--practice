#Containers with most water using Two-Pointers approach
heights = list(map(int, input().split()))
left, right = 0, len(heights)-1
area = 0
while left<right:
  width = right - 1
  height = min(heights[left], heights[right])
  area = max(area, width*height)
  if hieghts[left] < heights[right]:
    left+=1
  else:
    right+=1
print(area)

#Example Input: [1,8,6,2,5,4,8,3,7]
#Output: 49
