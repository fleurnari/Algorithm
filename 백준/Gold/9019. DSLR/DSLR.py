import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  visitList = [False for _ in range(10001)]
  queue = deque()
  queue.append((a, ''))
  visitList[a] = True

  while queue:
    n, c = queue.popleft()

    if n == b:
      print(c)
      break

    d = n * 2 % 10000
    if not visitList[d]:
      visitList[d] = True
      queue.append([d, c + 'D'])

    s = (n - 1) % 10000
    if not visitList[s]:
      visitList[s] = True
      queue.append([s, c + 'S'])

    l = n // 1000 + (n % 1000) * 10
    if not visitList[l]:
      visitList[l] = True
      queue.append([l, c + 'L'])

    r = n // 10 + (n % 10) * 1000
    if not visitList[r]:
      visitList[r] = True
      queue.append([r, c + 'R'])