import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n, k = map(int, input().split())
  d = list(map(int, input().split()))
  graph = [[] for _ in range(n + 1)]
  indegree = [0 for _ in range(n + 1)]
  dpTable = [0 for _ in range(n + 1)]
  queue = deque()
  
  for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

  w = int(input())

  for i in range(1, n + 1):
    if indegree[i] == 0:
      queue.append(i)
      dpTable[i] = d[i - 1]

  while queue:
    tmp = queue.popleft()

    for i in graph[tmp]:
      indegree[i] -= 1
      dpTable[i] = max(dpTable[i], dpTable[tmp] + d[i - 1])
      if indegree[i] == 0:
        queue.append(i)

  print(dpTable[w])