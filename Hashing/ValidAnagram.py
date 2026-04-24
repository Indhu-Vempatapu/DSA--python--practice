#only used to check if two strings are anagrams 
def ValidAnagram(s, t):
  if len(s) != len(t):
    return False
  count = {}
  for char in s.lower():
    count[char] = count.get(char, 0) + 1
  for char in t.lower():
    if t not in count:
      return False
    count[c] -= 1
    if count[c]<1:
      return False
  return True
s = input("enter a string: ")
t = input("enter another string: ")
print(ValidAnagram(s,t))

#Example: s=listen t=silent 
#Output: True

#Example: s=joy t=rat
#Output: False
