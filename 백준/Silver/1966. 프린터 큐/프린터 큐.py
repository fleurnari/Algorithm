import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  inputList = list(map(int, input().split()))
  q = deque(inputList)
  cnt = 0

  while q:
    primary = max(q)
    front = q.popleft()
    m -= 1

    if primary == front:
      cnt += 1
      if m < 0:
        print(cnt)
        break
    else:
      q.append(front)
      if m < 0:
        m = len(q) - 1