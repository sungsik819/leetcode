class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))

# l1 노드에서 숫자 추출하여 리스트 생성
node = l1
nums1 = []

while node != None:
  nums1.append(node.val)
  node = node.next

# l2 노드에서 숫자 추출하여 리스트 생성
node = l2
nums2 = []

while node != None:
  nums2.append(node.val)
  node = node.next

# 숫자를 가지고 자릿수에 관계 없이 숫자 계산
nums1.reverse()
nums2.reverse()
num1 = int("".join(map(str, nums1)))
num2 = int("".join(map(str, nums2)))
sum = list(map(int, str(num1 + num2)))
sum.reverse()

# 계산된 값으로 ListNode 계산
result = ListNode(sum[0])
rest = sum[1:]
move = result

for v in rest:
  move.next = ListNode(v)
  move = move.next