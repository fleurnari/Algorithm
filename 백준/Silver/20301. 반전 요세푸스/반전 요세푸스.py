import sys
from collections import deque
input = sys.stdin.readline
n, k, m = map(int, input().split())
dq = deque(range(1, n + 1))
direction = 1
cnt = 0

while dq:
  if direction == 1:
    dq.rotate(-(k - 1))
    print(dq.popleft())
  else:
    dq.rotate(k - 1)
    print(dq.pop())
  cnt += 1
  if cnt % m == 0:
    direction *= -1