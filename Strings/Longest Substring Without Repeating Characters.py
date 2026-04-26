def LongestSubstring(s):
  characters = {}
  l = 0 #left
  maximum = 0 #max length
  for r in range(len(s)):
    if s[r] in characters:
      l = max(l, characters[s[r]]+1)
    characters[s[r]] = r
    maximum = max(maximum, r-l+1)
  return maximum
s = input("enter a string: ")
print(LongestSubstring(s))

#Example Input : pwwkewxpw
#Output: 5
