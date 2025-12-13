import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)
  indegree[b] += 1

queue = deque()

for i in range(1, n + 1):
  if indegree[i] == 0:
    queue.append(i)

while queue:
  now = queue.popleft()
  print(now, end = ' ')
  for i in arr[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      queue.append(i)