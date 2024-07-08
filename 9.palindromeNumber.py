value1 = 121
value2 = -121

def palindrome(x: int):
  strx = str(x)
  rstrx = strx[::-1]

  if strx == rstrx:
    return True
  return False

print(palindrome(value2))