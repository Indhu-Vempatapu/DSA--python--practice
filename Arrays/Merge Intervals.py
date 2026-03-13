#Merge Intervals
def mergeIntervals(intervals):
  intervals.sort(key=lambda x:x[0])
  merged = []
  for interval in intervals:
    if not merged or merged[-1][1]<interval[0]:
      merged.append(interval)
    else:
      merged[-1][1]=max(merged[-1][1],interval[1])
  return merged
  
n = int(input("enter number of intervals: "))
intervals = []
for i in range(n):
  start , end = map(int, input().split())
  intervals.append([start, end])

if n<=1:
  print(intervals)
  exit()
else:
  print(mergeIntervals(intervals))              
