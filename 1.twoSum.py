
nums = [2, 7, 11, 15]
target = 9

def solution1():
  result = []
  for idx, _  in enumerate(nums):
    for idx2, _ in enumerate(nums):
      # 같은 인덱스인 경우 거른다.
      if nums[idx] + nums[idx2] == target and idx != idx2:
        result.extend([idx, idx2])
        break
    if len(result) > 0:
      break

  print(result)

def solution2():
  result = []
  for i, v in enumerate(nums):
    num = target - v
    try:
      index = nums.index(num)
      result.extend([i, index])
      break
    except ValueError:
      continue

  print(result)



if __name__ == "__main__":
  solution2()