strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]

minStr = min(strs1, key=len)
for i, x in enumerate(minStr):
  for other in strs1:
    if other[i] != x:
        print(minStr[:i])

print(minStr)
