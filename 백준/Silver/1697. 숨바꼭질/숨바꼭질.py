import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
max = 10 ** 5
visitList = [0] * (max + 1)

def bfs(v):
  queue = deque()
  queue.append(v)

  while queue:
    current = queue.popleft()
    if current == k:
      return visitList[k]
    for i in (current - 1, current + 1, current * 2):
      if 0 <= i <= max and not visitList[i]:
        visitList[i] = visitList[current] + 1
        queue.append(i)

print(bfs(n))