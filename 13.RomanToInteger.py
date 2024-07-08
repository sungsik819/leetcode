import re

s = 'III' # 3
s2 = 'LVIII' # 58
s3 = 'MCMXCIV' # 1994

# 패턴
# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
# IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900

# 2번째열에 있는 조건 부터 검색 후, 빼기?
pattern = {
  'I': 1, 
  'V': 5, 
  'X': 10, 
  'L': 50, 
  'C': 100, 
  'D': 500, 
  'M': 1000,
}

def getnumber(num: str):
  arabic = 0
  for i in range(len(num)):
      value = pattern[num[i]]
      if i < len(num)-1 and value < pattern[num[i+1]]:
          arabic -= value
      else:
          arabic += value

  return arabic

def getnumber2(num: str):
  arabic = 0
  for c1, c2 in zip(num, num[1:]):
      print(c1)
      value = pattern[c1]
      if value < pattern[c2]:
          arabic -= value
      else:
          arabic += value

  return arabic

print(getnumber2(s3))