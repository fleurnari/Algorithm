import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visitList = [False] * (n + 1)

for _ in range(m):
  s, e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)

for i in range(n + 1):
  graph[i].sort()

def dfs(v):
  visitList[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visitList[i]:
      dfs(i)

dfs(v)
print()

def bfs(v):
  queue = deque()
  queue.append(v)
  visitList[v] = True
  while queue:
    now = queue.popleft()
    print(now, end = ' ')
    for i in graph[now]:
      if not visitList[i]:
        visitList[i] = True
        queue.append(i)

visitList = [False] * (n + 1)
bfs(v)